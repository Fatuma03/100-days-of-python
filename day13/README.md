\# 100 Days of Python

🗓️ \*\*Day 13 – Debugging\*\*



\*\*Date:\*\* 2025-10-23  

\*\*Time spent:\*\* ~1–2 hrs



\## What I practiced

\- Reading and fixing error messages (`ModuleNotFoundError` for `maths`).

\- Tracing logic with print statements (checking intermediate values).

\- Verifying edge cases (FizzBuzz combined condition, leap year rule).



\## Bugs I found \& fixes

\- `import maths` → removed; no such module (and `math.add` doesn’t exist).

\- Replaced `maths.add(new\_item, item)` with `new\_item + item`.

\- In `fizz\_buzz`, `print(\[number])` → `print(number)` to avoid printing a list.

\- Confirmed leap-year logic with examples (1900 ❌, 2000 ✅, 2024 ✅).



\## Files

\- `day13/main.py` – mutate list, leap-year checker, FizzBuzz.



\## Notes / reflections

\- Start with the \*first\* error, fix it, run again.

\- Prefer simple arithmetic over importing libraries you don’t need. - For combined conditions (FizzBuzz), check the \*\*both\*\* condition first.

