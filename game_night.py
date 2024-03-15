# Task 1: Random Choice Game
# Create a game where a player has to guess the random item picked by the computer from a list.
# Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not.

import random

items = ['circle', 'triangle', 'square', 'rectangle', 'diamond']
player_guess = input("What item will it be circle/ triangle/ square/ rectangle/ diamond? : ")
rand_item = random.choice(items)
if rand_item == player_guess:
    print("You guessed correctly!")
else:
    print(f"You guessed wrong. The correct answer was: {rand_item}. Try again!")