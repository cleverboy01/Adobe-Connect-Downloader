## 2024-05-24 - File Hashing I/O Overhead
**Learning:** Performing many small reads (e.g., 64 iterations of 4KB chunks) for file hashing introduces significant I/O system call overhead compared to reading a larger chunk at once.
**Action:** When extracting fixed-size headers for hashing, use a single `read()` operation with a dynamically calculated size (e.g., `self.config.video_hash_chunk_size * 64`) to minimize syscalls while preserving configuration flexibility.
