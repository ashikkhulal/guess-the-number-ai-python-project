import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0 
    print(f"\nWelcome to Guess the Number Game!\n\n\
        The rule of this game is simple:\n\
        AI has picked up a random number between 1 and {x}.\n\
        And you need the guess that number correctly\n\n\
        Now give it a go...\n")
    while guess != random_number:
        guess = int(input("Please enter your guess: "))
        if guess < random_number:
            print(f"Sorry, guess again. Too low. Guess again!\n")
        elif guess > random_number:
            print(f"Sorry, guess again. Too high. Guess again!\n")

    print(f"Yay, congrats. You have correctly guessed the random number ({random_number}) that was between 1 and {x}!!!")

guess(1000)