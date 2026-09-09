## 2024-10-24 - Network Optimization
**Learning:** Found an N+1 query problem where the primary meeting URL was being fetched multiple times to extract different metadata (`recording_id` and `account_id`).
**Action:** Batched metadata extraction into a single network request to minimize I/O and reduce TTFB impact when analyzing URLs before download.
