## 2024-05-24 - Responsive CLI Progress Bars
**Learning:** Hardcoding `ncols` (e.g., `ncols=80`) for `tqdm` progress bars in CLI applications can lead to ugly terminal truncation on narrower screens, and underutilizes space on wider screens.
**Action:** Always use `dynamic_ncols=True` to ensure the progress bar automatically adapts to the terminal width. Additionally, using `colour='green'` adds a subtle but effective visual distinction to the progress bar, improving the overall CLI UX.
