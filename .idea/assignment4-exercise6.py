import random


def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    # Calculate the approximate value of pi
    pi_approximation = 4 * points_inside_circle / num_points

    return pi_approximation


def main():
    # Ask the user for the number of random points
    num_points = int(input("Enter the number of random points to generate: "))

    # Calculate the approximate value of pi
    pi_approximation = approximate_pi(num_points)

    # Print the approximation of pi
    print("Approximation of pi:", pi_approximation)


if __name__ == "__main__":
    main()
