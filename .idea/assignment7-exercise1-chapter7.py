# Define seasons
seasons = ('winter', 'spring', 'summer', 'autumn')

# Define month boundaries for each season
month_boundaries = {
    'winter': (1, 2, 3),
    'spring': (4, 5, 6),
    'summer': (7, 8, 9),
    'autumn': (10, 11, 12)
}

# Get input from user
month = int(input("Enter the number of a month (1-12): "))

# Determine the season
for season, months in month_boundaries.items():
    if month in months:
        print(f"The month {month} is in {season}.")
        break
