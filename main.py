# A Python Project to build a game called "Rock Paper Scissors"

# Importing the random module
import random

# Creating a list of play options
t = ["rock", "paper", "scissors"]

# Assign a random play to the computer
computer = t[random.randint(0,2)]


# Set player to False
player = False

while player == False:
    # Set player to True
    player = input("Rock, Paper, Scissors?: ")
    if player.lower() == computer:
        print("Computer chooses", computer.capitalize())
        print("You choose", player.capitalize())
        print("Tie!")
    elif player.lower() == "rock":
        if computer == "paper":
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Lose! " + computer.capitalize(), "covers", player.capitalize())
        else:
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Win! " + player.capitalize(), "smashes", computer.capitalize())
    elif player.lower() == "paper":
        if computer == "scissors":
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Lose! " + computer.capitalize(), "cut", player.capitalize())
        else:
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Win! " + player.capitalize(), "covers", computer.capitalize())
    elif player.lower() == "scissors":
        if computer == "rock":
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Lose! " + computer.capitalize(), "smashes", computer.capitalize())
        else:
            print("Computer chooses", computer.capitalize())
            print("You choose", player.capitalize())
            print("You Win! " + computer.capitalize(), "covers", computer.capitalize())
    elif player.lower()=="quit":
        print("Thanks for playing!")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    # Reset the game loop and start over again
    player = False
    computer = t[random.randint(0,2)]

# End of the game
