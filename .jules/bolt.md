## 2024-05-24 - Eliminate Redundant HTTP Requests
**Learning:** The application previously performed redundant `session.get` requests for the same URL in `get_id_and_type` and `get_account_id`, causing unnecessary network overhead. Relying on a global cache can fail with `requests.Session`. Passing response text directly avoids redundancy.
**Action:** Refactored the core workflow to fetch HTML once and pass the resulting text to downstream parsing functions. This pattern prevents duplicate network calls while maintaining session integrity.
