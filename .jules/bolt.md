## 2024-10-23 - Redundant HTTP Requests with Requests Session
**Learning:** Passing response data (like HTML text) directly to subsequent functions is faster and more correct than making redundant HTTP requests or using global URL-based caching dictionaries, which typically fail to account for `requests.Session` context.
**Action:** Always check if subsequent functions can reuse data already fetched by previous functions within the same flow, rather than repeating HTTP requests.
