## 2024-09-13 - [Caching HTML Response to Avoid Redundant Network Latency]
**Learning:** Found redundant API calls to fetch HTML content of the recording page. Specifically, `get_id_and_type` and `get_account_id` were independently fetching the exact same URL. Network latency in downloading redundant web pages is a clear performance bottleneck.
**Action:** Always fetch page content once at the top level and pass `html_content` strings to downstream parsing functions, rather than passing request session objects and letting each function re-fetch the data.
