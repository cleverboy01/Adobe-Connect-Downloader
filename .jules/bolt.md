## 2024-05-24 - [Avoid Redundant Network Requests]
**Learning:** Found multiple functions making overlapping HTTP GET requests to the same URL to extract different IDs from the HTML text. Network IO was a major unoptimized path.
**Action:** Always inspect helper functions that process external resources to see if they re-fetch data rather than accepting the data payload as a parameter.
