import random

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)

# Main program to roll the dice until the result is 6
def main():
    while True:
        result = roll_dice()
        print("Result of the dice roll:", result)
        if result == 6:
            break

# Call the main function to execute the program
main()
