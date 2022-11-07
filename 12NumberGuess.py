#12th day challenge
#Making number guessing game

import random

print("Welcome to the number guessing game!")
difficulty = input("Choose a difficulty. Type Easy or Hard: ").lower()

def choose_difficulty(user_diff):
    if user_diff == "easy":
        return 10
    elif user_diff == "hard":
        return 5

def give_hint(user_guess):
    if guess_number > user_guess:
        print("Too low\nGuess again")
        return False
    elif guess_number < user_guess:
        print("Too high\nGuess again")
        return False
    elif guess_number == user_guess:
        print(f"You got it. Number was {guess_number}")
        return True

life = choose_difficulty(difficulty)
guess_number = random.randint(1, 100)

while life > 0:
    user_numberguess = int(input("Guess number: "))
    check = give_hint(user_numberguess)
    if check is False:
        life = life - 1
        print(f"You have {life} attempts remaining to guess the number")
    elif check is True:
        break