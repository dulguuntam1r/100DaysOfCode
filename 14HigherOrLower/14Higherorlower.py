from game_data import data
from os import system
from random import randint

print("Welcome to Higher or Lower game !")


def check_follower(name_a, name_b, player_input):
    if player_input == "a":
        if data[name_a]["follower_count"] >= data[name_b]["follower_count"]:
            return True
    elif player_input == "b":
        if data[name_a]["follower_count"] <= data[name_b]["follower_count"]:
            return True

def print_info(name_a, name_b):
    print(f'Compare A: {data[name_a]["name"]}, a {data[name_a]["description"]}, from {data[name_a]["country"]}')
    print("Versus")
    print(f'Compare B: {data[name_b]["name"]}, a {data[name_b]["description"]}, from {data[name_b]["country"]}')

def next_turn():
    global a
    global b
    global score
    a = b
    b = randint(0, len(data) - 1)
    score = score + 1
            

a = randint(0, len(data) - 1)
b = randint(0, len(data) - 1)
score = 0

while True:
    print_info(a, b)
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if check_follower(a, b, guess) == True:
        next_turn()
        system('cls')
        print(f"You're right! Current score: {score}")
    else:
        system('cls')
        print(f"You lost with score of {score}")
        break