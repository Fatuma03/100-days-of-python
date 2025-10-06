# Day 09 - Secret Auction (Dictionaries) 
 
**Concepts:** dictionaries, loops, user input, finding a max value 
 
## What it does 
Collects bids as name -> amount and prints the highest bidder. 
 
## How to run 
python main.py 
 
## Notes I learned 
- Using a dict to map name -> bid 
- Getting the max value safely 
- Basic input validation (strip(), isdigit()) 
 
## Next improvements 
- Save bids to a file 
- Currency formatting for outputs 
## Notes I learned
- Stored bids in a **dictionary** as name - (e.g., {"Ali": 120}).
- Wrote **find_highest_bidder(dct)** to scan keys and track a running max.
- Used a **while loop** with a boolean flag (bidding=True) to keep asking for input.
- Normalized answers with **.lower()** so 'YES'/'Yes' still work.
- Kept non-number input safe by converting bid with **int(...)** (plan to validate).

## Gotchas / fixes I noticed
- Clearing the screen with print("\n" * 20) works but better to use **cls** on Windows.
- If two people tie, current code picks the **first** it saw; consider handling ties.

## Next improvements
- Validate bids: re-prompt until a positive integer is entered.
- Use **max(dict, key=dict.get)** for a cleaner highest-bidder.
- Replace newline clear with **os.system("cls")** on Windows.
