 # ProxyBolt

 ## Overview  
 🚀 **Supercharge your proxy scraping with ProxyBolt!** 🚀  
 ProxyBolt is a **blazing-fast**, asynchronous proxy scraper and verifier built for **security pros, web developers, and sysadmins**. With an incredible **400+ proxies/sec verification speed**, it delivers unmatched efficiency! ⚡️


 ## Key Features
 - **Asynchronous Proxy Scraping:** Utilize asyncio and aiohttp for non-blocking, high-speed proxy collection. ⚙️
 - **Dynamic Concurrency Control:** Automatically scales verification tasks based on real-time CPU load and memory, reaching up to 800 concurrent tasks! 📈
 - **Lightning-Fast Verification:** Combines a rapid TCP handshake with HTTP GET requests to validate proxies in record time. 🚀
 - **Real-Time Progress Monitoring:** Watch the magic happen with an interactive progress bar powered by tqdm_asyncio. ⏱️
 - **CSV Output:** Export your verified proxies to CSV for seamless integration. 💾
 - **Modular Codebase:** Clean, scalable design using modern Python best practices. 🧩

 ## Quickstart
 **One-Liner to Clone, Install & Run:**
 ```
 git clone https://github.com/chernistry/ProxyBolt.git && cd ProxyBolt && pip install -r requirements.txt && python3 -m proxybolt.main
 ```

 <div align="center">
   <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
   <img src="https://img.shields.io/badge/Version-2.0.0-green" alt="Version">
   <img src="https://img.shields.io/github/stars/chernistry/ProxyBolt?style=social" alt="Stars">
 </div>


 ## Configuration
 Manage all settings via `src/proxybolt/config.toml`. Key parameters include:
 - **output_dir & output_file:** Destination for your verified proxies CSV.
 - **request_timeout:** HTTP request timeout in seconds.
 - **scrape_threads:** Number of concurrent proxy scraping tasks (default: 100).
 - **check_threads:** Maximum concurrent verification tasks (default: 800).
 - **tcp_quick_timeout:** Fast TCP handshake timeout (default: 1.5 seconds).
 - **test_url:** URL used for proxy responsiveness testing (default: "https://www.linkedin.com").

 ## Usage
 **Run ProxyBolt:**
 ```
 python3 -m proxybolt.main
 ```
 ProxyBolt will:
 - **Scrape:** Collect proxies from multiple trusted sources.
 - **Verify:** Dynamically adjust concurrency and verify proxies in real-time.
 - **Export:** Save the top-performing proxies to a CSV file.

 ## Directory Structure
 ```
 ProxyBolt/
 ├── LICENSE
 ├── ProxyBolt.iml
 ├── README.md
 ├── pyproject.toml
 ├── requirements.txt
 └── src
     └── proxybolt
         ├── __init__.py
         ├── checker.py
         ├── config.py
         ├── config.toml
         ├── main.py
         ├── output.py
         ├── scraper.py
         └── utils.py
 ```

 ## Performance Optimization & Monitoring
 - **uvloop:** Integrated for a high-performance event loop that supercharges asynchronous processing. ⚡️
 - **Dynamic Concurrency:** Monitors CPU and memory in real time using psutil, adjusting task limits to optimize performance. 📊
 - **Real-Time Progress Bar:** Live progress updates during proxy verification keep you informed every step of the way. ⏳


 ## Contribution Guidelines
 We welcome your contributions! To get involved:
 1. **Fork** the repository.
 2. **Create a feature branch:** `git checkout -b feature/your-feature-name`.
 3. **Follow coding standards:** Adhere to project conventions and include relevant tests.
 4. **Submit a pull request** with detailed descriptions, screenshots, and code comments.

 ## Additional Resources
 - **Documentation:** Detailed docs and usage examples are available on our Wiki.
 - **Community & Support:** Join the discussion on [GitHub Discussions](https://github.com/chernistry/ProxyBolt/discussions).

 ## License & Credits
 - **License:** MIT License © 2025 ProxyBolt Contributors
 - **Credits:** Special thanks to our amazing open-source community and all contributors.

**ProxyBolt** is engineered for rapid deployment and seamless integration in security and web scraping environments. Its cutting-edge asynchronous design, dynamic scaling, and visually appealing interface meet the demands of modern developers and enterprises. Star, fork, and contribute to join our fast-growing community!


 ## Contact
 For inquiries or support, please email: [sanderchernitsky@gmail.com](mailto:sanderchernitsky@gmail.com)

 GitHub Repository: [https://github.com/chernistry/ProxyBolt](https://github.com/chernistry/ProxyBolt)
