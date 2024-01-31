# Ask the user for biological gender and hemoglobin value
gender = input("Enter biological gender (male/female): ").lower()
hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

# Define normal hemoglobin ranges
normal_range_female = (117, 155)
normal_range_male = (134, 167)

# Check the gender and hemoglobin level
if gender == "female" and normal_range_female[0] <= hemoglobin_value <= normal_range_female[1]:
    print("Hemoglobin level is normal for a female.")
elif gender == "male" and normal_range_male[0] <= hemoglobin_value <= normal_range_male[1]:
    print("Hemoglobin level is normal for a male.")
else:
    print("Hemoglobin level is outside the normal range.")
