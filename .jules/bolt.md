## 2024-05-30 - Redundant HTTP Requests with `requests.Session`
**Learning:** Passing `requests.Session` around and making redundant `session.get()` calls to the same URL in `get_id_and_type` and `get_account_id` (called from `construct_zip_urls`) causes unnecessary network overhead. Fetching the HTML once and passing it directly as text eliminates duplicate requests and avoids unsafe global caches.
**Action:** Centralize the initial `session.get()` in the main processing function and pass the resulting `response.text` string directly to `get_id_and_type` and `get_account_id`.
