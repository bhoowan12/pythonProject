import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Flag to control the loop
guessed_correctly = False

# Loop until the user guesses the correct number
while not guessed_correctly:
    # Ask the user to guess the number
    guess = int(input("Guess the number between 1 and 10: "))

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
        guessed_correctly = True
