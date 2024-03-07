class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.floor_up(target_floor)
        elif target_floor < self.current_floor:
            self.floor_down(target_floor)
        else:
            print("Elevator is already on floor", target_floor)

    def floor_up(self, target_floor):
        while self.current_floor < target_floor and self.current_floor < self.top_floor:
            self.current_floor += 1
            print("Elevator is now on floor", self.current_floor)

    def floor_down(self, target_floor):
        while self.current_floor > target_floor and self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print("Elevator is now on floor", self.current_floor)

# Main program
if __name__ == "__main__":
    # Create an elevator instance
    my_elevator = Elevator(1, 10)

    # Move the elevator to the 5th floor
    my_elevator.go_to_floor(5)

    # Move the elevator back to the bottom floor
    my_elevator.go_to_floor(1)
