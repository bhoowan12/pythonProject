# Define the correct username and password
correct_username = "python"
correct_password = "rules"

# Initialize the number of attempts
attempts = 0

# Loop for login attempts
while attempts < 5:
    # Ask the user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect username or password. Please try again.")
        attempts += 1

# Check if the maximum number of attempts reached
if attempts == 5:
    print("Access denied")
