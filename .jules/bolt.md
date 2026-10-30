## 2024-05-24 - Eliminating Redundant HTTP Requests
**Learning:** When eliminating redundant HTTP requests involving sessions, prefer passing response data (e.g., HTML text) directly to subsequent functions rather than using global URL-based caching dictionaries. Global caches typically fail to account for `requests.Session` context, potentially introducing security or correctness risks.
**Action:** Extract and pass the HTML response from the initial `get_id_and_type` request downstream to `construct_zip_urls` and `get_account_id` to avoid a redundant `session.get()` call.
