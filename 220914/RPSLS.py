    import random

victories = {
    "rock": ["scissors", "lizard"],
    "scissors": ["paper", "lizard"],
    "paper": ["spock", "rock"],
    "spock": ["rock", "scissors"],
    "lizard": ["paper", "spock"]
    }
RPSLS = list(victories.keys())

def winner_decide(p1_ans, p2_ans):
    if p1_ans == p2_ans:
        return 0
    p1_defeats = victories[p1_ans]
    if p2_ans in p1_defeats:
        return 1
    return 2

game = True

while game:
    player_ans = ""
    while player_ans.lower() not in RPSLS:
        player_ans = input("rock, paper, scissors, Spock or lizard? ").lower()
    bot_ans = random.choice(RPSLS)
    print("You choose", player_ans)
    print("Computer choose", bot_ans)
    winner = winner_decide(player_ans, bot_ans)
    if winner == 0:
        print("Tie!")
    elif winner == 1:
        print("You win!")
    else:
        print("You lose!")
    continue_playing = ""
    while continue_playing != "yes" and continue_playing != "no":
        continue_playing = input("Do you want to play again, yes or no? ").lower()
    if continue_playing == "yes":
        continue
    elif continue_playing == "no":
        print("You sucks!")
        break
