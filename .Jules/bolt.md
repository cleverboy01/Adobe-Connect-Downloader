## 2024-10-24 - [FFmpeg Log Parsing Bottleneck]
**Learning:** Parsing high-frequency FFmpeg logs line-by-line using generic regex matching without early returns incurs unnecessary CPU overhead on non-matching lines.
**Action:** Always pre-compile regex patterns and implement fast-path early returns (e.g., `if "substring" not in line:`) before invoking regex searches in hot loops.
