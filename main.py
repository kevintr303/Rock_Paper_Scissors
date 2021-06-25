import random

moves = ["rock", "paper", "scissors"]
winners = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


# Ask the user for their move
def user_move(move=None):
    while move not in ["1", "2", "3"]:
        move = input("choose a move:\n1: rock\n2: paper\n3: scissors\n\nmove: ")
    return moves[int(move) - 1]


# Make the bot choose a move
def bot_move():
    return random.choice(moves)


# Check the winner of the game
def check_winner(user, bot):
    if user == bot:
        return f"You tied! You both chose {user}."
    return (
        f"You won! The bot chose {bot}"
        if bot == winners[user]
        else f"You lost. The bot chose {bot}."
    )


# Ask if the user wants to play again
def play_again(response=None):
    while response not in ["y", "n"]:
        response = input("Do you want to play again? [y/n] ")
    return True if response == "y" else False


if __name__ == "__main__":
    while True:
        print(check_winner(user_move(), bot_move()))
        if play_again():
            continue
        break
