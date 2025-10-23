
# number = random.randint(1,100)
# print(number)
# print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': " ).lower()
# if difficulty == 'easy':
#     attempts = 10
# else:
#     attempts =5
# print(f"You have {attempts} attempts remaining to guess the number.")
# continue_game = True
# while continue_game:
#     guess = int(input("Make a guess: "))
#     if guess > number:
#         attempts -=1
#         print(f"Too high\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
#         if attempts ==0:
#             continue_game = False
#             print("Too high\nYou've run out of the guesses, you Lose")
#     elif guess < number:
#         attempts -=1
#         print(f"Too low\nGuess again\nYou have {attempts} attempts remaining to guess the number.")
#         if attempts ==0:
#             continue_game = False
#             print("Too low\nYou've run out of the guesses, you Lose")
#     else:
#         print(f"You got it! The answer was {number}\nGuess again")
#         continue_game = False
import random
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

#function to check user's guess against actual number
def check_answer(user_guess, actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}\nGuess again")
        return None
def game():
    print(logo)
    #choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"The correct answer {answer}")
    #let the user guess a number
    turns = set_difficulty()

    guess = 0
    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns ==0:
            print("You've run out of the guesses, you Lose")
            return

    #Track the number of turns and reduce by 1 if they get it wrong

game()

