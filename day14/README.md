\# 100 Days of Python  

🗓️ \*\*Day 14 — Higher Lower Game (Project)\*\*  

\*\*Date:\*\* 2025-11-04  

\*\*Time spent:\*\* ~2–3 hrs





\## Files

\- `day14/main.py` — game loop and logic.

\- `day14/art.py` — ASCII `logo` and `vs`.

\- `day14/game\_data.py` — `data` list of accounts (each dict has `name`, `description`, `country`, `follower\_count`).



---



\## How it works

1\. Randomly pick two accounts (\*\*A\*\* and \*\*B\*\*).

2\. Show their info using:

&nbsp;  ```python

&nbsp;  def format\_data(account):

&nbsp;      return f"{account\['name']}, a {account\['description']}, from {account\['country']}"

Ask the user: Who has more followers? 'A' or 'B'?



Check correctness with:



python



def check\_answer(user\_guess, a\_followers, b\_followers):

&nbsp;   if a\_followers > b\_followers:

&nbsp;       return user\_guess == 'a'

&nbsp;   else:

&nbsp;       return user\_guess == 'b'

If correct, add to score and keep the winner for the next round; bring in a new challenger.



Example run



Compare A: Taylor, a musician, from USA

VS

Against B: Messi, a footballer, from Argentina

Who has more followers? Type 'A' or 'B': a



You're right! Current score 1

What I learned

Returning comparisons directly (e.g., user\_guess == 'a') gives a boolean (True/False) you can return immediately.



Normalize input so 'A', ' a ', etc. still work: guess = input(...).strip().lower().



Keep A and B from being identical; if they match, repick B.



(Optional) Handle ties by rerolling B if a\_followers == b\_followers.



How to run

bash

Copy code

python day14/main.py

