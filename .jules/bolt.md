## 2024-05-15 - Redundant Metadata HTTP Requests
**Learning:** The URL analysis phase was making two separate HTTP requests for the same exact URL to extract different IDs (`recording_id` and `account_id`) via different functions (`get_id_and_type` and `get_account_id`).
**Action:** Always combine URL metadata extraction into a single function and single HTTP request. We now parse the single response text for both IDs.
