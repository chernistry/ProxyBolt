# src/proxybolt/utils.py

import time
import logging
from contextlib import asynccontextmanager
import psutil
from proxybolt.config import GENERAL_CONFIG

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@asynccontextmanager
async def profile(section: str):
    start = time.monotonic()
    try:
        yield
    finally:
        elapsed = time.monotonic() - start
        logging.info(f"[PROFILE] {section} took {elapsed:.3f}s")

async def dynamic_concurrency() -> int:
    # Measure CPU load over a short interval (0.1 sec)
    load = psutil.cpu_percent(interval=0.1) / 100.0
    mem_avail = psutil.virtual_memory().available / (1024**3)  # in GB
    max_concurrency = GENERAL_CONFIG.check_threads  # now 800 from config.toml
    adjusted = int((1 - load) * (mem_avail / 0.5) * max_concurrency)
    # Ensure a minimum of 50 concurrent tasks
    return min(max_concurrency, max(50, adjusted))
