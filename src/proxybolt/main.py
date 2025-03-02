import asyncio
import logging
import aiohttp
import uvloop
from tqdm.asyncio import tqdm_asyncio
from proxybolt import scraper, checker, output, utils, config

async def main():
    uvloop.install()  # High-performance event loop
    logging.info("Starting ProxyBolt proxy scraper...")

    # Scrape proxies with profiling
    async with utils.profile("Scraping proxies"):
        proxies = await scraper.gather_proxies()
    proxies_list = list(proxies)
    logging.info(f"Scraped {len(proxies_list)} proxies.")

    # Use dynamic concurrency (targeting up to check_threads from config)
    concurrency = await utils.dynamic_concurrency()
    logging.info(f"Using dynamic concurrency limit: {concurrency}")
    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, ssl=False)

    verified_results = []
    async with aiohttp.ClientSession(connector=connector) as session:
        async def limited_check(proxy: str):
            async with semaphore:
                return await checker.verify_proxy(session, proxy)
        tasks = [limited_check(proxy) for proxy in proxies_list]
        # Iterate over tasks using tqdm_asyncio.as_completed to show progress bar
        for coro in tqdm_asyncio.as_completed(tasks, total=len(tasks), desc="Verifying proxies"):
            try:
                success, elapsed, prx = await coro
                if success:
                    verified_results.append((prx, elapsed))
            except Exception as e:
                logging.debug(f"[MAIN] Error verifying proxy: {e}")

    verified_results.sort(key=lambda x: x[1])
    logging.info(f"[MAIN] {len(verified_results)} proxies verified successfully.")

    async with utils.profile("Saving proxies to CSV"):
        output.write_proxies_to_csv(verified_results)
    logging.info("ProxyBolt finished. Verified proxies saved.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
    input("Done. Press Enter to exit...")
