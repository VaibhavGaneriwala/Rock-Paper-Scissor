# A Python Project to build a game called "Rock Paper Scissors"

# Importing the random module
import random

# Creating a list of play options
options = ["rock", "paper", "scissors"]

# Assign a random play to the computer
computer = options[random.randint(0,2)]

# Set player to False
player = False

def output():
    print("Computer chooses", computer.capitalize())
    print("You choose", player.capitalize())

def play():
    global player
    global computer
    while player == False:
        # Set player to True
        player = input("Rock, Paper, Scissors?: ")
        if player.lower() == computer:
            print("You both chose", player.capitalize())
            print("Tie!")
        elif player.lower() == "rock":
            if computer == "paper":
                output()
                print("You Lose! " + computer.capitalize(), "covers", player.capitalize())
            else:
                output()
                print("You Win! " + player.capitalize(), "smashes", computer.capitalize())
        elif player.lower() == "paper":
            if computer == "scissors":
                output()
                print("You Lose! " + computer.capitalize(), "cut", player.capitalize())
            else:
                output()
                print("You Win! " + player.capitalize(), "covers", computer.capitalize())
        elif player.lower() == "scissors":
            if computer == "rock":
                output()
                print("You Lose! " + computer.capitalize(), "smashes", computer.capitalize())
            else:
                output()
                print("You Win! " + computer.capitalize(), "covers", computer.capitalize())
        elif player.lower()=="quit":
            print("Thanks for playing!")
            break
        else:
            print("That's not a valid play. Check your spelling!")
        # Reset the game loop and start over again
        player = False
        computer = options[random.randint(0,2)]

# calling the play function
play()
# End of the game