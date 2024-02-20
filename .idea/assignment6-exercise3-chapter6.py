# Function to convert gallons to liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541  # 1 gallon is approximately equal to 3.78541 liters
    return liters

# Main program to ask for volume in gallons and convert to liters
def main():
    while True:
        gallons = float(input("Enter the volume in gallons (negative to quit): "))
        if gallons < 0:
            print("Exiting the program...")
            break
        liters = gallons_to_liters(gallons)
        print("Volume in liters:", liters)

# Call the main function to execute the program
main()
