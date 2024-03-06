class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

# Main program
if __name__ == "__main__":
    # Create a new car instance
    my_car = Car("ABC-123", 142)

    # Print out all the properties of the new car
    print("Registration Number:", my_car.registration_number)
    print("Maximum Speed:", my_car.max_speed, "km/h")
    print("Current Speed:", my_car.current_speed, "km/h")
    print("Travelled Distance:", my_car.travelled_distance, "km")
