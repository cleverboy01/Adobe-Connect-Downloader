## 2026-09-24 - Consolidating API Calls
**Learning:** This codebase previously performed two separate HTTP GET requests to the same URL to parse different metadata (recording ID and account ID). This N+1 style inefficiency during initialization slows down batch processing significantly.
**Action:** Always inspect initialization or metadata fetching phases to ensure all necessary regex/parsing is done in a single pass over one network request.
