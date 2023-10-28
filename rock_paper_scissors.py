import random

choices = ["rock", "paper", "scissors"]

player_choice = input("Rock, paper, or scissors? ")
computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print("Tie")
elif player_choice == "rock" and computer_choice == "scissors":
    print("Player wins")
elif player_choice == "scissors" and computer_choice == "paper":
    print("Player wins")
elif player_choice == "paper" and computer_choice == "rock":
    print("Player wins")
else:
    print("Computer wins")
