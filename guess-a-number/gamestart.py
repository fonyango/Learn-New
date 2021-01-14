#Creating a guess a number game
import random

number = random.randrange(1, 10)
guess = int(input("Guess a number between 1 and 10: "))
guesses = 1

while guess != number:
    if guess < number:
        print("You need to guess higher. Try again please")
        guess = int(input("\nGuess a number between 1 and 10: "))
        guesses = guesses + 1

    else:
        print("You need to guess lower. Try again please")
        guess = int(input("\nGuess a number between 1 and 10: "))
        guesses = guesses + 1

print()
print("Congratulations! Your guess is correct!")
print("It only took you", guesses, "guesses!")

