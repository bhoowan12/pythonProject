# Initialize an empty list to store numbers
numbers = []

# Continue taking input until an empty string is entered
while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the user wants to quit
    if user_input == "":
        break

    # Try to convert the input to a float
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if any numbers were entered
if numbers:
    # Print the smallest and largest numbers
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers entered.")
