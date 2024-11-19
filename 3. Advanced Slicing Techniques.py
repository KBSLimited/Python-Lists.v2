#Task 1: Given list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract temperatures for the second week (index 7 to index 14)
second_week_temps = temperatures[7:15]

# Output the result
print(f"Temperatures for the second week: {', '.join(map(str, second_week_temps))}")

#Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.
above_100 = [temp for temp in temperatures if temp > 100]

# Output the result
print(f"Temperatures above 100: {', '.join(map(str, above_100))}")