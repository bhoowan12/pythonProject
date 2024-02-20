# Initialize an empty list to store city names
cities = []

# Ask the user to enter the names of five cities
print("Enter the names of five cities:")
for i in range(5):
    city = input(f"City {i+1}: ")
    cities.append(city)

# Print the names of the cities one by one
print("Cities entered:")
for city in cities:
    print(city)
