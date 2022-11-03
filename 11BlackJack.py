#11th day challenge
#Capstone project: Blackjack game

import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
blackjack = {
    "User": {
        "Score": 0,
        "Cards": []
    },
    "Dealer": {
        "Score": 0,
        "Cards": []
    }
}

def calculate_score():
    for players in blackjack:
        blackjack[players]["Score"] = sum(blackjack[players]["Cards"])

def user_score():
    if blackjack["User"]["Score"] > 21:
        for cards in range(len(blackjack["User"]["Cards"])):
            if blackjack["User"]["Cards"][cards] == 11:
                blackjack["User"]["Cards"][cards] = 1
        calculate_score()
    return blackjack["User"]["Score"]

def dealer_score():
    if blackjack["Dealer"]["Score"] > 21:
        for cards in range(len(blackjack["Dealer"]["Cards"])):
            if blackjack["Dealer"]["Cards"][cards] == 11:
                blackjack["Dealer"]["Cards"][cards] = 1
        calculate_score()
    return blackjack["Dealer"]["Score"]

def clear_score():
    for players in blackjack:
        blackjack[players]["Cards"].clear()
    calculate_score()

def print_score(stage):
    print(f'Your cards: {blackjack["User"]["Cards"]}, Score: {blackjack["User"]["Score"]}')
    if stage == 1:
        print(f'Dealer first card: {blackjack["Dealer"]["Cards"][0]}')
    else:
        print(f'Dealer cards: {blackjack["Dealer"]["Cards"]}, Score: {blackjack["Dealer"]["Score"]}')

def game_initiate():
    for players in blackjack:
        blackjack[players]["Cards"] = random.choices(cards, k=2)
        calculate_score()

while True:
    start_game = input("Do you want to play game of blackjack: Yes or No?\n").lower()
    if start_game == "no":
        print("Goodbye!")
        break
    elif start_game == "yes":
        clear_score()
        game_initiate()
    else:
        print("Wrong input")
        break
    while True:
        system('cls')
        print_score(1)
        if dealer_score() == 21:
            print_score(2)
            print("Dealer wins")
            break
        elif user_score() == 21:
            print_score(2)
            print("You win")
            break
        card_draw = input("Do you want another card? Yes or No\n").lower()
        if card_draw == "yes":
            blackjack["User"]["Cards"].append(random.choice(cards))
            calculate_score()
            if user_score() > 21:
                print_score(2)
                print("Dealer wins")
                break
        elif card_draw == "no":
            while dealer_score() < 17:
                blackjack["Dealer"]["Cards"].append(random.choice(cards))
                calculate_score()
            print_score(2)
            if dealer_score() > 21:
                print("You win")
            elif user_score() > dealer_score():
                print("You win")
            elif user_score() == dealer_score():
                print("Draw")
            else:
                print("Dealer wins")
            break
        else:
            print("Wrong input")
            break