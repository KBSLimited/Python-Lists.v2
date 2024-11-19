#Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

#Task 2: Calculate the average grade and print it.
grades = [95, 93, 90, 89, 88, 85, 80, 78, 76, 72]
average_grade = sum(grades) / len(grades)
print(f"Average grade: {average_grade:.2f}")