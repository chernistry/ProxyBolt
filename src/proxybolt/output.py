# src/proxybolt/output.py

import csv
import time
from pathlib import Path
import logging
from typing import List, Tuple
from proxybolt.config import GENERAL_CONFIG

def write_proxies_to_csv(proxies: List[Tuple[str, float]]) -> None:
    output_dir = Path(GENERAL_CONFIG.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / GENERAL_CONFIG.output_file
    with output_file.open("w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["proxy", "response_time", "timestamp"])
        timestamp = int(time.time())
        for proxy, response_time in proxies:
            writer.writerow([proxy, f"{response_time:.3f}", timestamp])
    logging.info(f"[OUTPUT] Saved {len(proxies)} proxies to {output_file.resolve()}")
