# src/proxybolt/config.py

import toml
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Dict

CONFIG_PATH = Path(__file__).parent / "config.toml"

@dataclass
class GeneralConfig:
    output_dir: str
    output_file: str
    request_timeout: float
    scrape_threads: int
    check_threads: int
    tcp_quick_timeout: float
    test_url: str

@dataclass
class FullConfig:
    general: GeneralConfig
    regex: Dict[str, Any]
    sources: Dict[str, Any]  # Each key (e.g. "HTTP", "HTTPS", etc.) contains its source dict

def load_config() -> FullConfig:
    if not CONFIG_PATH.exists():
        raise FileNotFoundError(f"Configuration file not found at {CONFIG_PATH}")
    config_data = toml.load(CONFIG_PATH)
    general = config_data.get("general", {})
    regex = config_data.get("regex", {})
    sources = config_data.get("sources", {})

    general_cfg = GeneralConfig(
        output_dir=general.get("output_dir", "./output"),
        output_file=general.get("output_file", "proxies.csv"),
        request_timeout=general.get("request_timeout", 30.0),
        scrape_threads=general.get("scrape_threads", 50),
        check_threads=general.get("check_threads", 600),
        tcp_quick_timeout=general.get("tcp_quick_timeout", 1.5),
        test_url=general.get("test_url", "https://www.linkedin.com")
    )
    return FullConfig(general=general_cfg, regex=regex, sources=sources)

# Global configuration objects
CONFIG = load_config()
GENERAL_CONFIG = CONFIG.general
SOURCES_CONFIG = CONFIG.sources
