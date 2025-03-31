
import random

def play_game():
  choices = ["rock", "paper", "scissors"]
  computer = random.choice(choices)

  user = input("Do you choose rock, paper or scissors? :").lower()
  while user not in choices:
    user = input("Invalid choice. Please enter rock, paper or scissors: ").lower()

  print(f"\nComputer chose {computer}")

  if user == computer:
    return "It's a tie!"

  if (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
     return "You win!"
  return "You lose!"
print(play_game())
print("THANK YOU FOR PLAYING!")

