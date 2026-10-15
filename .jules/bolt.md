## 2024-05-14 - File Read Overhead Optimization
**Learning:** Found a performance bottleneck in `detector/caching.py` where the file hashing algorithm performs 64 sequential `read()` operations of 4KB chunks. This introduces significant I/O system call overhead, especially given it's done repeatedly.
**Action:** Replaced the loop with a single `read()` operation computing the total required bytes dynamically using `self.config.video_hash_chunk_size * 64`. This reduces system calls from 64 to 1 while retaining the same functionality.
