
import art
import random

print(art.logo)
print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100.")
numbers = range(1,101)
number=random.choice(numbers)
print(f"Psst, the correct answer is {number}")
print("Choose a difficulty. Type easy or hard")
input_difficulty = input().lower()
if input_difficulty == "easy":
  attempts = 10
else:
  attempts = 5

while attempts > 0:
    print("Make a guess.")
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Enter your guess: "))
    if guess == number:
       print(f"You got it! The answer was {number}.")
       break
    elif guess < number:
      print("Too low.")
    else :
      print("Too high.")
    attempts -= 1
    print(f"Attempts remaining: {attempts}")

if attempts == 0:
    print("You've run out of guesses, you lose.")
    print(f"The correct answer was {number}.")