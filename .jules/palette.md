## 2024-05-24 - Progress Bar UX
**Learning:** Hardcoding `ncols=80` for tqdm progress bars can lead to truncation or messy terminal output on different window sizes.
**Action:** Use `dynamic_ncols=True` and `colour='green'` to ensure progress bars adapt to terminal width and provide clear visual feedback without truncation.
