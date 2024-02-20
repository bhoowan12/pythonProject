import random

# Ask the user how many dice to roll
num_dice = int(input("How many dice to roll? "))

# Initialize the sum of dice rolls
total = 0

# Roll each die and accumulate the total
for _ in range(num_dice):
    roll = random.randint(1, 6)  # Assuming 6-sided dice
    print("Roll:", roll)
    total += roll

# Print the total sum of the dice rolls
print("Total sum:", total)
