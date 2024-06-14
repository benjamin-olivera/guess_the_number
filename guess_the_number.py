
print("Welcome to the Number Guess Game!")
print("I'm thinking of a number between 1 and 100.")

import random
numbers = range(1,101)
number=random.choice(numbers)
print(f"Psst, the correct answer is {number}")
print("Choose a difficulty. Type esay or hard)")
input_difficulty = input().toLowerCase()
if input_difficulty == "easy":
  attempts = 10
else:
  attempts = 5

while attempts > 0:
    print("Make a guess.")
    print(f"You have{attempts} attempts remaining to guess the number.")
    guess = input("Enter your guess: ")
    if guess == number:
       print("You got it! The answer was {number}.")
    elif guess < number:
       print("Too low.")
    else :
        print("Too high.")