## 2023-10-20 - Optimize File Hashing Read Calls
**Learning:** Multiple small read calls inside a loop (`f.read(chunk)` repeated 64 times) introduces unnecessary system call overhead in Python when hashing file headers.
**Action:** When extracting a fixed-size header for caching or hashing, read the required bytes in a single `read()` call, computing the size dynamically from existing configs (e.g. `config.chunk_size * count`). This yields a measurable performance boost.
