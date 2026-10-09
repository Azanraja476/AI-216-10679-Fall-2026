# Lab 04 — Python Data Structures & Clean Code

## Concepts Practiced
- Lists, tuples, dictionaries, and sets
- Comprehensions (list, dictionary, set)
- `enumerate()` and `zip()` iteration tools
- Aliasing, shallow copying, and deep copying
- Hashability and tuples as dictionary keys
- Clean code architecture and multi-file organization

## Tasks Completed
1. Working with Lists (`append`, `extend`, slicing, sorting)
2. Aliasing vs Copying (Shallow vs Deep copy)
3. Tuples for Fixed Data & Dictionary Keys
4. Dictionaries for Structured Records
5. Sets for Unique Labels & Validation
6. Comprehensions
7. `enumerate()` and `zip()`
8. Data Structure Selection
9. Prediction Analysis (Refactoring & Handling Inconsistent/Incomplete Records)
10. Optional Per-Label Confidence Report

## Clean-Code Refactoring
- Separated data preprocessing (`preprocessing.py`), statistical analysis (`analysis.py`), and script coordination (`main.py`).
- Replaced magic values with named constants (e.g., `MIN_CONFIDENCE`, `ALLOWED_LABELS`).
- Handled incomplete and inconsistent records without mutating raw input data.