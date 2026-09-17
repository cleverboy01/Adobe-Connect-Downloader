## 2024-05-18 - [CLI Terminal UX Coloring]
**Learning:** Adding colors to tqdm progress bars (using `colour='cyan'` or `colour='green'`) is a very simple and high-impact UX win for CLI tools, providing immediate visual differentiation between different phases of execution (e.g., downloading vs encoding).
**Action:** Use this pattern across Python CLI tools that employ `tqdm` to break up the monochrome terminal output and help users track multi-step processes at a glance.
