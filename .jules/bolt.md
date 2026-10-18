## 2024-05-18 - File Hashing I/O Overhead
**Learning:** Using many small chunked reads (e.g., 64 reads of 4KB) for hashing files introduces significant I/O system call overhead compared to a single read of the same total size.
**Action:** When extracting fixed-size headers for hashing, use a single `read()` operation with a dynamically calculated total size (e.g., `chunk_size * 64`) to preserve configuration flexibility while avoiding the loop overhead.
