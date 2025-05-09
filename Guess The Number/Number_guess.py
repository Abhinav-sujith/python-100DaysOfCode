# code 

from art import logo
from random import randint

print(logo)
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")


chosen = int(input("Make a guess: "))
actual_number = randint(1,100)

def compare_numbers(chosen_number, game_number):
    if chosen_number > game_number:
        return "higher"
    elif chosen_number < game_number:
        return "lower"
    else:
        return "equal"

def run_game(level):
    if level == "hard":
        attempts = 5
    elif level == "easy":
        attempts = 10
    #more difficulties if wanted



compare_numbers(chosen,actual_number)

# Previous Attempts 


"""
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
def easy():
    print("You have 5 attempts remaining to guess the number")
    random_number = random.randint(1, 100)
    attempts = 5
    for chances in range(attempts):
        chosen_number = 0
        guess = int(input(f"Make a guess: {chosen_number}"))
        chosen_number += guess
        if chosen_number == random_number:
            print("You have guess the correct number")
            break
        if chosen_number >= random_number:
            print("Too high")
            print(guess)
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
        if chosen_number <= random_number:
            print("Too low")
            print(guess)
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
    print(f"The random number is {random_number}")

def hard():
    print("You have 10 attempts remaining to guess the number")
    random_number = random.randint(1,100)
    attempts = 10
    for chances in range(attempts):
        chosen_number = 0
        guess = int(input(f"Make a guess: {chosen_number}"))
        chosen_number += guess
        if chosen_number == random_number:
            print("You have guess the correct number")
            break
        if chosen_number >= random_number:
            print("Too high")
            print(guess)
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")
        if chosen_number <= random_number:
            print("Too low")
            print(guess)
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number")

    print(f"The random number is {random_number}")

if level == "easy":
    easy()
if level == "hard":
    hard()

"""

"""import random
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
TURNS  = 0
def check_answer(user_guess,actual_answer, turns):
    "Checks answer against guess, returns the number of turns remaining"
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return  turns - 1
    else:
        print(f"You got it! the answer was {actual_answer}")


def game():
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")
    answer = randint(1,100)
    print(f"The correct answer is {answer}")

    # function to set difficulty
    def set_difficulty():
        level = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()
        if level == "easy":
            return  EASY_LEVEL_TURNS
        else:
            return HARD_LEVEL_TURNS

    turns = set_difficulty()

    # let the user guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input("make a guess"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses you lose")
            return
        elif guess != answer:
            print("Guess again")
game()"""
