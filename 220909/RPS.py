import random

moves = ["rock", "paper", "scissors"]
while True:
    player_answer = ""
    while player_answer != "rock" and player_answer != "paper" and player_answer != "scissors":
        player_answer = input("rock, paper or scissors? ")
        player_answer = player_answer.lower()
    computer_answer = random.choice(moves)
    print("computer move is", computer_answer)
    if computer_answer == player_answer:
        print("It's a tie!")
    elif (player_answer == "rock" and computer_answer == "scissors") \
    or (player_answer == "paper" and computer_answer == "rock") \
    or (player_answer == "scissors" and computer_answer == "paper"):
        print("Player wins!")
    else:
        print("Computer wins!")
    continue_playing = ""
    while continue_playing != "yes" and continue_playing != "no":
        continue_playing = input("Do you want to play again, yes or no? ").lower()
    if continue_playing == "yes":
        continue
    elif continue_playing == "no":
        print("You sucks!")
        break
