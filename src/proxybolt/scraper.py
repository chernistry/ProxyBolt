# src/proxybolt/scraper.py

import re
import itertools
import asyncio
import aiohttp
import logging
from typing import List, Set
from proxybolt.config import GENERAL_CONFIG, SOURCES_CONFIG

# Precompiled regex for binary extraction of proxies
PROXY_BIN_PATTERN = re.compile(rb'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+')

def parse_proxies(content: bytes) -> List[str]:
    """Extract and decode proxy strings from binary content."""
    return [proxy.decode("utf-8", errors="ignore") for proxy in PROXY_BIN_PATTERN.findall(content)]

async def fetch_url(session: aiohttp.ClientSession, url: str) -> List[str]:
    try:
        async with session.get(url, timeout=GENERAL_CONFIG.request_timeout, ssl=False) as resp:
            content = await resp.read()
            return parse_proxies(content)
    except Exception as e:
        logging.debug(f"[SCRAPE] Error fetching {url}: {e}")
        return []

async def gather_proxies() -> Set[str]:
    """Concurrently fetch proxies from all source URLs and deduplicate them."""
    # Flatten all URLs from all sources (each source is expected to have a "urls" list)
    urls = list(itertools.chain(*[v.get("urls", []) for v in SOURCES_CONFIG.values()]))
    all_proxies: Set[str] = set()
    connector = aiohttp.TCPConnector(limit=GENERAL_CONFIG.scrape_threads, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for proxy_list in results:
            all_proxies.update(proxy_list)
    logging.info(f"[SCRAPE] Fetched {len(all_proxies):,} unique proxies.")
    return all_proxies
