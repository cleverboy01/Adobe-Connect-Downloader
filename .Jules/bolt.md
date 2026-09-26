## 2024-05-24 - Network Request Reduction and Connection Pooling
**Learning:** The application was making redundant GET requests to the same URL for extracting different IDs, and creating a new requests.Session for every URL in a batch, failing to utilize connection pooling.
**Action:** Caching the HTML response from the initial request to parse subsequent IDs, and reusing a single requests.Session across batch downloads, significantly improves network throughput and processing speed.
