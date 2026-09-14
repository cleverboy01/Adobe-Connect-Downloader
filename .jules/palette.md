## 2024-10-24 - Active Progress Indicators for Unknown Durations
**Learning:** In CLI applications, when processing durations are unknown (e.g., streaming downloads or asynchronous tasks where duration cannot be probed), using static `print` statements creates anxiety because the user cannot tell if the app is frozen.
**Action:** Always provide an active progress indicator (like `tqdm` with `total=None`), which shows elapsed time and activity (iterations/seconds processed), assuring the user that the process is still running.
