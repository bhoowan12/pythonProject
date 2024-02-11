# Initialize an empty list to store numbers
numbers = []

# Ask the user to input numbers until they input an empty string
while True:
    num_input = input("Enter a number (or press Enter to quit): ")
    if num_input == '':
        break
    else:
        # Convert the input to float and append to the list
        numbers.append(float(num_input))

# Sort the numbers in descending order and get the five greatest numbers
greatest_numbers = sorted(numbers, reverse=True)[:5]

# Print the five greatest numbers
print("The five greatest numbers are:", greatest_numbers)
