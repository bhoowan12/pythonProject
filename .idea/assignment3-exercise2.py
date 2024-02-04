while True:
    # Ask the user to enter the value in inches
    inches = float(input('Enter the value in inches (enter a negative value to end): '))

    # Check if the user wants to end the program
    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters
    centimeters = inches * 2.54

    # Print the result
    print(f"{inches} inches is equal to {centimeters} centimeters.")
