#Ninth day challenge
#Secret auction game where bidders don't know each others bid

import os

bidders = {}
print("Welcome to our auction !!!")

def add_bidders(name, amount):
    bidders[name] = amount

game_end = False

while not game_end:
    username = input("What is your name?\n")
    user_bid = int(input("What is your bid amount?\n$"))
    add_bidders(username, user_bid)
    other_user = input("Is there any other bidder? yes or no\n").lower()
    if other_user == "no":
        game_end = True
    elif other_user == "yes":
        os.system('cls')
    
highest_bidder = max(bidders, key=bidders.get)
print(f"The winner of the auction is {highest_bidder} with amount of ${bidders[highest_bidder]}")


#Instructer used code below to find highest bidder using for loop
# def find_highest_bidder(bidding_record):
#   highest_bid = 0
#   winner = ""
#   for bidder in bidding_record:
#     bid_amount = bidding_record[bidder]
#     if bid_amount > highest_bid: 
#       highest_bid = bid_amount
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")
