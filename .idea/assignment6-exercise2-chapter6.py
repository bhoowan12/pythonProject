import random

# Function to simulate a dice roll with variable number of sides
def roll_dice(num_sides):
    return random.randint(1, num_sides)

# Main program to roll the dice until the maximum number is rolled
def main():
    num_sides = int(input("Enter the number of sides on the dice: "))
    while True:
        result = roll_dice(num_sides)
        print("Result of the dice roll:", result)
        if result == num_sides:
            break

# Call the main function to execute the program
main()
