import random

RPSLS = ["rock", "paper", "scissors", "spock", "lizard"]
def check_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def check_winner(player_answer, computer_answer):
    player_answer = RPSLS.index(player_answer)
    computer_answer = RPSLS.index(computer_answer)
    if player_answer == computer_answer:
        return 1
    if check_odd((player_answer-computer_answer) % 5):
        return 2
    return 0

score = 0
level = 1
round_ = 1
game = True
while game:
    print("--------------------------------------------------------------")
    print("level =", level, ", round =", round_)
    player_answer = ""
    while player_answer not in RPSLS:
        player_answer = input("rock, paper, scissors, spock or lizard? ").lower()
    bot_answer = random.choice(RPSLS)
    winner_score = check_winner(player_answer, bot_answer)
    score = score + winner_score
    print("player choose", player_answer)
    print("Computer choose", bot_answer)
    if winner_score == 1:
        print("It's a tie in this round!", "your score:", score)
    elif winner_score == 2:
        print("You win this round!", "your score:", score)
    else:
        print("You lose this round!", "your score:", score)
    if round_ == 5:
        if score < level*5:
            print("Tham nam, ngu dot, con dung cai lit")
            break
        elif level == 3 and score >= 15:
            print("Dong dat a? Ko phai, day la ban dang di len.")
            break
        else:
            level = level + 1
            round_ = 1
            print("Ban da tu day xa hoi len 1 buoc")
    else:
        round_ = round_ + 1
