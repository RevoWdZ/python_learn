import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    user = None

    while user not in choices:
        user = input("Select a weapon (Rock, Paper, Scissors): ").lower()

    if user == computer:
        print("Tie!")

    elif user == "rock":
        if computer == "paper":
            print("Computer wins!")
        if computer == "scissors":
            print("U win!")

    elif user == "paper":
        if computer == "scissors":
            print("Computer wins!")
        if computer == "rock":
            print("U win!")

    elif user == "scissors":
        if computer == "rock":
            print("Computer wins!")
        if computer == "paper":
            print("U win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye")
