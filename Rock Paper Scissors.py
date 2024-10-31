# Write your code here :-)
#Rock, Paper, Scissors Game
import random

#moves for the player
moves = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(moves)
    player = input("rock, paper or scissors? (or end the game) ").lower()
    if player == "end the game":
        print("The game has ended.")
        break
    elif player == computer:
            print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose, paper beats rock")
        else:
            print("You win, rock beats scissors")

    elif player == "paper":
        if computer == "scissors":
            print("You lose, scissors beats paper")
        else:
            print("You win, paper beats rock")

    elif player == "scissors":
        if computer == "rock":
            print("You lose, rock beats scissors")
        else:
            print("You win, scissors beats paper")



