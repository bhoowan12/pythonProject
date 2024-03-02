class AirportData:
    def __init__(self):
        self.airports = {}

    def add_airport(self, icao, name):
        self.airports[icao] = name

    def get_airport_name(self, icao):
        return self.airports.get(icao, "Airport not found")

def main():
    airport_data = AirportData()

    while True:
        print("\nMenu:")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            icao = input("Enter the ICAO code of the airport: ")
            name = input("Enter the name of the airport: ")
            airport_data.add_airport(icao, name)
            print("Airport added successfully!")

        elif choice == '2':
            icao = input("Enter the ICAO code of the airport: ")
            name = airport_data.get_airport_name(icao)
            print(f"The name of the airport is: {name}")

        elif choice == '3':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
