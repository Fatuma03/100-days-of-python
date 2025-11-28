\# Day 15 — Coffee Machine ☕ (Functions, State, CLI)



\*\*Date:\*\* 2025-10-??  

\*\*Time spent:\*\* ~2–3 hrs



\## Goals

\- Practice procedural decomposition with small, focused functions.

\- Track machine \*\*resources\*\* (water, milk, coffee) and \*\*money\*\*.

\- Handle \*\*coin input\*\* and transaction validation (insufficient funds / change).

\- Support commands: `espresso`, `latte`, `cappuccino`, `report`, `off`.



---



\## Files

\- `day15/main.py`



---



\## What I learned / notes

\- Using dictionaries to model the \*\*MENU\*\* and \*\*resources\*\*.

\- Separating concerns:

&nbsp; - `is\_resource\_sufficient()` → check stock before accepting payment

&nbsp; - `process\_coins()` → total quarters/dimes/nickels/pennies

&nbsp; - `is\_transaction\_successful()` → compare cost, handle change, update profit

&nbsp; - `make\_coffee()` → deduct ingredients, print confirmation

\- Building a clean CLI loop with `while is\_on:` and commands (`report`, `off`, drink names).



---



\## Key snippet

```python

\# from day15/main.py

def is\_resource\_sufficient(order\_ingredients):

&nbsp;   for item in order\_ingredients:

&nbsp;       if order\_ingredients\[item] > resources\[item]:

&nbsp;           print(f"Sorry there is not enough {item}.")

&nbsp;           return False

&nbsp;   return True



def process\_coins():

&nbsp;   print("Please insert coins")

&nbsp;   total = int(input("How many quarters: ")) \* 0.25

&nbsp;   total += int(input("How many dimes: ")) \* 0.10

&nbsp;   total += int(input("How many nickels: ")) \* 0.05

&nbsp;   total += int(input("How many pennies: ")) \* 0.01

&nbsp;   return total

Sample run



What would you like? (espresso/latte/cappuccino): latte

Please insert coins

How many quarters: 12

How many dimes: 0

How many nickels: 0

How many pennies: 0

Here is your $0.5 in change

Here is your latte ☕️. Enjoy!



What would you like? (espresso/latte/cappuccino): report

Water: 100

Milk: 50

Coffee: 76

Money: 2.5



Try: `report`, then `espresso/latte/cappuccino`, and a case with not enough resources.



&nbsp;\*\*Day 15:\*\* \[Coffee Machine](day15/README.md)

