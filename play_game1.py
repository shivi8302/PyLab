import random

# List of words to guess
words = ["apple", "banana", "cherry", "date", "litchi"]

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the guessed letters
guessed = ["_"] * len(word)

# Create a set to store the incorrect guesses
incorrect = set()

# Number of attempts left
attempts = 6

print("Welcome to Hangman!")
print("You have 6 attempts to guess the word.")

while attempts > 0:
  # Show the current state of the word
  print(" ".join(guessed))
  print(f"Incorrect guesses: {', '.join(incorrect)}")
  print(f"Attempts left: {attempts}") 
  #print("attempts left:", attempts)

  # Ask the user for a guess
  guess = input("Guess a letter: ")

  # Check if the guess is in the word
  if guess in word:
    # Reveal the correct guess
    for i in range(len(word)):
      if word[i] == guess:
        guessed[i] = guess
  else:
    # Add the incorrect guess to the set
    incorrect.add(guess)
    attempts -= 1

  # Check if the word has been completely guessed
  if "_" not in guessed:
    print("Congratulations, you won!"'\n'"The word is",word)
    break
else:
  print(f"Game over! The word was {word}.")

