# src/proxybolt/checker.py

import asyncio
import time
import aiohttp
import logging
from typing import Tuple
from proxybolt.config import GENERAL_CONFIG

async def verify_proxy(session: aiohttp.ClientSession, proxy: str) -> Tuple[bool, float, str]:
    """
    1. Attempts a TCP connection to quickly rule out unresponsive proxies.
    2. If successful, performs an HTTP GET request to the test URL.
    Returns a tuple (success, response_time, proxy).
    """
    try:
        ip, port_str = proxy.split(':')
        port = int(port_str)
        await asyncio.wait_for(
            asyncio.open_connection(ip, port),
            timeout=GENERAL_CONFIG.tcp_quick_timeout
        )
    except Exception:
        return (False, 0.0, proxy)

    start = time.monotonic()
    try:
        resp = await asyncio.wait_for(
            session.get(GENERAL_CONFIG.test_url, proxy=f"http://{proxy}", ssl=False),
            timeout=GENERAL_CONFIG.request_timeout
        )
        async with resp:
            if resp.status < 400:
                elapsed = time.monotonic() - start
                return (True, elapsed, proxy)
    except Exception as e:
        logging.debug(f"[CHECK] Proxy {proxy} failed HTTP check: {e}")
    return (False, 0.0, proxy)
