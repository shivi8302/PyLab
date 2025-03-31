import random

def play_game():
  number_to_guess = random.randint(1, 100)
  attempts = 0
  while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if user_guess < number_to_guess:
      print("Too low! Try again.")
    elif user_guess > number_to_guess:
      print("Too high! Try again.")
    else:
      print(f"Congratulations! You found the number in {attempts} attempts.")
      break

play_game()
