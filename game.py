# game.py

import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("USER_NAME")

print(z) # reads the variable from the environment

print("Welcome to")
print("Rock, Paper, Scissors, Shoot!")

#Ask for user input
#source: https://docs.python.org/3/library/functions.html#input

x = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(x)

#validate user input


if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("VALID")
else:
    print("OOPS, INVALID, PLEASE TRY AGAIN")
    exit()


print("User chose: ",x)

#generate computer choice
#https://docs.python.org/3/library/random.html
#source: https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list


valid_options = ["rock", "paper", "scissors"] #list

c = random.choice(valid_options)
print("Computer Chose:", c)
#determine the winner of the game


#determine if we won or lost
#inspired by https://www.geeksforgeeks.org/python-if-else/#if-else
#user picks rock, paper or signer VS computer random generation.
if x == c:
    print("It's a tie, try again")
elif x == "rock" and c == "paper":
    print ("You Lose! Play again")
elif x ==  "rock" and c == "scissors":
    print ("You win! Yay!")
elif x == "paper" and c == "rock":
    print ("You win! Yay!")
elif x == "paper" and c == "scissors":
    print ("You lose! Better luck next time.")
elif x == "scissors" and c == "rock":
    print ("You lose! Sorry!")
elif x == "scissors" and c == "paper":
    print ("You win! Awesome!")


print("Hope you come back soon!")