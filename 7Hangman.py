#Seventh day challenge
#Hangman game

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

#chosen_word = random.choice(word_list) was easier way
chosen_word = word_list[random.randint(0, len(word_list) - 1)]
display = []
for letter in chosen_word:
    display.append("_")

game_end = False
lives = 6

while not game_end:
    chosen_letter = input("Guess a letter:").lower()
    if chosen_letter in display:
        print(f"You have already guessed {chosen_letter}")
    for index in range(len(chosen_word)):
        if chosen_letter == chosen_word[index]:
            display[index] = chosen_letter
    if chosen_letter not in chosen_word:
        lives -= 1
        print(f"{chosen_letter} is not in the word")
    print(f"{' '.join(display)}")
    print(stages[lives])
    if "_" not in display:
        game_end = True
        print("You won !!!")
    if lives == 0:
        game_end = True
        print("You lost !!!")