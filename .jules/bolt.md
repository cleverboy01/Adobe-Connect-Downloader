## 2024-05-24 - Redundant HTTP Requests in adobe_downloader.py
**Learning:** Found that `get_id_and_type` and `get_account_id` perform redundant GET requests to the same URL in sequence. This occurs when resolving recording details.
**Action:** Introduce a caching layer (`_html_cache`) or pass the response text directly when calling these consecutive functions to avoid redundant HTTP calls.
