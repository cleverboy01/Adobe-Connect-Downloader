## 2024-05-15 - Batched Metadata Extraction
**Learning:** In URL processing loops, extracting multiple metadata fields via separate HTTP requests to the same endpoint causes a severe N+1 performance bottleneck.
**Action:** Always batch related metadata extraction into a single HTTP request, especially when parsing identical HTML responses.
