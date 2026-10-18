## 2024-05-14 - Tqdm Progress Bar UX Pattern
**Learning:** Hardcoding `ncols` in `tqdm` progress bars can cause terminal truncation on narrow terminals, leading to a poor user experience.
**Action:** Use `dynamic_ncols=True` to allow the progress bar to adapt to terminal width. Also, adding `colour='green'` improves visual clarity and gives positive feedback during operations.
