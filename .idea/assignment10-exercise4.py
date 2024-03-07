import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-20, 20))
            car.drive(1)

    def print_status(self):
        print("Race:", self.name)
        print("{:<15} {:<15} {:<15} {:<15}".format("Car", "Speed (km/h)", "Distance (km)", "Travel Time (hours)"))
        for car in self.cars:
            print("{:<15} {:<15} {:<15} {:<15}".format(car.registration_number, car.current_speed, car.travelled_distance, car.travel_time))

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.travel_time = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
        self.travel_time += hours

# Main program
if __name__ == "__main__":
    # Create cars
    cars = []
    for i in range(1, 11):
        car = Car("Car " + str(i), random.randint(100, 200))
        cars.append(car)

    # Create race
    grand_demo_race = Race("Grand Demolition Derby", 8000, cars)

    # Simulate race progress
    hour_count = 0
    while not grand_demo_race.race_finished():
        grand_demo_race.hour_passes()
        hour_count += 1
        if hour_count % 10 == 0:
            grand_demo_race.print_status()

    # Print final status
    grand_demo_race.print_status()
