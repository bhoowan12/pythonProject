# Function to remove odd numbers from a list
def remove_odd_numbers(input_list):
    even_numbers = [num for num in input_list if num % 2 == 0]
    return even_numbers

# Main program
def main():
    # Create a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to remove odd numbers
    cut_down_list = remove_odd_numbers(original_list)

    # Print both original and cut-down lists
    print("Original list:", original_list)
    print("Cut-down list (even numbers only):", cut_down_list)

# Call the main function to execute the program
main()
