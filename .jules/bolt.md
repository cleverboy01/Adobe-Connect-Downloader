## 2024-05-24 - Optimize video hashing I/O
**Learning:** Avoid many small chunked reads (e.g., 64 reads of 4KB) for file hashing as it introduces significant I/O system call overhead.
**Action:** Use a single read() operation for fixed-size headers, dynamically calculating the size based on configuration (e.g., config.video_hash_chunk_size * 64).