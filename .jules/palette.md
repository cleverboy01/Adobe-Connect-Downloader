## 2024-11-07 - tqdm Dynamic Resizing and Colour
**Learning:** Hardcoding `ncols=80` for tqdm progress bars leads to terminal truncation issues or poor utilization of space, especially in varying environments.
**Action:** Use `dynamic_ncols=True` and a `colour` parameter (like 'green') when initializing `tqdm` progress bars to prevent truncation and enhance visual clarity.
