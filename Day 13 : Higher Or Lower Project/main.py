# import logo

import random
from art import logo, vs
from game_data import data

# generating random account from the game data

def formatted_account(account):
    account_name = account["name"]
    account_desc  = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc} , from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return  user_guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Making account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"compare A: {formatted_account(account_a)}")
    print("vs")
    print(f"Compare B: {formatted_account(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n"*20)
    print(logo)

    ## - Get follower count of each account

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    # Check if user is correct.
    is_correct = check_answer(guess,a_follower_account,b_follower_account)

    # Give user feedback on their guess.
    # score keeping.

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False