# 100 Days of Python
🗓️ **Day 11  Blackjack (Functions, Logic, Loops)**
**Date:** 2025-10-09  
**Time spent:** ~2–3 hrs


## Goals
- Practice returning values and reusing logic across functions.
- Implement game rules (Blackjack check, dealer draw to 17).
- Handle edge cases (Ace as 11 -> 1, busts, draws).
- Structure a small CLI program cleanly.

---

## Files
- `day11/main.py`
- `day11/art.py`

---

## What I learned / notes
- Using a **sentinel score** (`0`) to represent Blackjack simplifies comparisons.
- Why `random.choice()` is better than `random.sample(..., 1)` when you need a single int.
- Difference between **returning values** vs **printing** (print for UI, return for logic).
- Managing state with loops/flags: `while not is_game_over:` then dealer logic.
- Ace handling: if `sum(hand) > 21` and `11 in hand` → convert one `11` to `1`.

---

## Key snippet

```python
# from day11/main.py
import random
from art import logo

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Return the score of a hand. 0 means Blackjack (two-card 21)."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score: return "Draw 🙃"
    elif c_score == 0:     return "Lose, opponent has a Blackjack 😱"
    elif u_score == 0:     return "Win with a Blackjack 🎉"
    elif u_score > 21:     return "You went over. You lose 😭"
    elif c_score > 21:     return "Opponent went over. You win 😁"
    elif u_score > c_score:return "You win 😊"
    else:                  return "You lose 😒"