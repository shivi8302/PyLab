import random

words = ["apple", "banana", "cherry", "date", "litchi"]

word = random.choice(words)

guessed = ["_"] * len(word)

incorrect = set()

attempts = 6

print("Welcome to Hangman!")
print("You have 6 attempts to guess the word.")

while attempts > 0:
  print(" ".join(guessed))
  print(f"Incorrect guesses: {', '.join(incorrect)}")
  print(f"Attempts left: {attempts}") 

  guess = input("Guess a letter: ")

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessed[i] = guess
  else:

    incorrect.add(guess)
    attempts -= 1

  if "_" not in guessed:
    print("Congratulations, you won!"'\n'"The word is",word)
    break
else:
  print(f"Game over! The word was {word}.")


nums=[1,2,3,4,5]
k=2

def rotate(nums,k: int) -> None:
    n=len(nums)
    for _ in range(k):
        last = nums[-1]
        for i in range(n-1,0,-1):
            print(nums)
            nums[i] = nums[i-1]
            print(nums)
            nums[0]=last
    return nums
rotate(nums,2)


