## 2024-05-24 - Network Request Deduplication
**Learning:** Found a performance bottleneck where multiple functions (`get_id_and_type` and `get_account_id`) were making identical HTTP GET requests to the same URL sequentially during the initial meeting analysis phase.
**Action:** Introduced a session-level cache (`session._page_cache`) to store the HTML response text of the first request. Subsequent functions needing the same page text now check this cache first, eliminating redundant network I/O and latency.
