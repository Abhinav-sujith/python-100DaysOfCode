# code

import random
from art import logo


def deal_cards():
    """return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """This function is going to take a list of cards and return thr sum of score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw :("
    elif c_score == 0:
        return "Lose opponent has black jack"
    elif u_score == 0:
        return "Win with a blackjack"
    elif u_score > 21:
        return "You went over. You lose"
    elif c_score > 21:
        return "opponent went over. You win"
    elif u_score > c_score:
        return "you win"
    else:
        return "you lose"

def play_game():
    print(logo)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {user_card} and computer card: {user_score}")
        print(f"Computers first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_continue = input("Type y to get another card, type n to stop")
            if user_should_continue == "y":
                user_card.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)



    print(f"Your final hand : {user_card} and your score is: {user_score}")
    print(f"Your final hand: {computer_card} and your computer score is: {computer_score}")
    print(compare_score(user_score,computer_score))

while input("Do you wanna play a game of black jack y or n ") == "y":
    print("\n"*30)
    play_game()
