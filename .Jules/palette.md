## 2024-05-18 - Improve tqdm progress bars UX
**Learning:** Hardcoded `ncols` limits and lack of color in CLI progress bars can lead to truncation in smaller terminals and less engaging user experience. The reusable UX pattern here is to apply `dynamic_ncols=True` and `colour='green'` to all `tqdm` initializations to improve readability and visual polish.
**Action:** Use `dynamic_ncols=True` and `colour='green'` whenever initializing `tqdm` progress bars in CLI tools.
