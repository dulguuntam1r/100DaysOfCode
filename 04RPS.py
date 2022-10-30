#Fourth day challenge
#Make Rock, Paper and Scissors game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

user_choice = int(input("What is your choice? Type 0 for rock, 1 for paper or 2 for scissors\n"))
computer_choice = random.randint(0, 2)

if (user_choice >= 3) or (user_choice < 0):
    print("You chose invalid number! You lose!")
    
else:
    print(f"Your choice:\n{rps[user_choice]}")
    print(f"Computer choice:\n{rps[computer_choice]}")
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice > computer_choice) or (user_choice == 0 and computer_choice == 2):
        print("You won!")
    else:
        print("Computer won!")
