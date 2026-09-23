## 2023-09-23 - Tqdm Progress Bar Enhancements
**Learning:** Hardcoding `ncols=80` or relying on default widths in tqdm progress bars can cause terminal truncation or awkward wrapping on varied screen sizes, and lack of color makes the output blend into other console logs.
**Action:** Always use `dynamic_ncols=True` to allow tqdm to resize to the terminal width dynamically, and add a `colour='green'` parameter to visually distinguish the progress bar from general log output.
