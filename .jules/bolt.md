## 2024-05-18 - Eliminated Redundant Network Requests
**Learning:** Found that the downloader was making duplicate HTTP GET requests to the exact same recording URL just to parse different pieces of metadata (SCO-ID vs Account ID). Network latency dominates CLI application performance in these extraction phases.
**Action:** When scraping or probing initial URLs, ensure all required metadata (ID, Account, Type, etc.) is extracted in a single combined network call rather than modularizing the network calls themselves.
