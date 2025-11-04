from game_data import data
import random
#import the logo's
from art import logo, vs
#function that takes the account data and prints in the printable format
def format_data(account):
    """Takes the account data and prints the printable format"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

#function that checks answer between user guess and a and b followers
def check_answer(user_guess,account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return user_guess == 'a'
    else:
        return user_guess == 'b'
#set score
score =0
game_should_continue = True
#randomly choose 2 accounts
print(logo)
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b= random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    #input more followers function
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    #dermining the account followers
    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']
    is_correct = check_answer(guess, a_followers, b_followers)
    if is_correct:
        score +=1
        print(f"You're right! Current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
