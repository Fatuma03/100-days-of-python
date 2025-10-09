# 100 Days of Python
### 🗓️ Day 10  Functions & Simple CLI
**Date:** 2025-10-08  
**Time spent:** ~2–3 hrs

**Goals**
- Practice functions that return values.
- Wire simple logic into a CLI program.

**Files**
- `day10/main.py`
- `day10/art.py`

**What I learned / notes**
- Difference between `print()` and `return`.
- How to structure a small program across files (importing from `art.py`).
- Basic input loop with validation.

**Key snippet**
```python
# from day10/main.py
from art import logo

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(logo)
    print(add(2, 3))  # expect 5

