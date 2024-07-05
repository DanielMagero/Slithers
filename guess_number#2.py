import random

guess_num = random.randint(1,20)

print("Welcome! \n Guess a number between 1 and 20.")

guess = 0

while guess != guess_num:
    print("Take your guess")
    guess = int(input())

    if guess > guess_num:
        print("Too high! Try again:")
    elif guess < guess_num:
        print("Too low! Try again:")
    else:
        print("Well guessed!")