# Initialize an empty set to store names
names_set = set()

# Iterate until an empty string is entered
while True:
    name = input("Enter a name (or press Enter to finish): ")

    # If name is empty, exit the loop
    if name == '':
        break

    # Check if the name is new or existing
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        # Add the new name to the set
        names_set.add(name)

# Print all the names
print("\nInput names:")
for name in names_set:
    print(name)
