import random

#Generate a random number between 1 and 20
secretNumber = random.randint(1,20)

print("Welcome to Dataframe Class Game")
print("I am thinking of a number between 1 and 20.")

guess = 0
guesses = 0

while guess != secretNumber:
    print("Take a guess")
    guess = int(input())

    guesses += 1

    if guess < secretNumber:
        print ("Your guess is too low")
    elif guess > secretNumber:
        print ("Your guess is too high")
    
    else:
        break

if guess == secretNumber:
    print(f"Good!!, You guessed my number in {str(guesses)} guesses.")
else:
    print(f"Nope the number I was thinking of is {str(secretNumber)}. ")
