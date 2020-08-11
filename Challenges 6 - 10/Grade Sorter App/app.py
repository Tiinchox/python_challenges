# Welcome message
print("Welcome to the Grade Sorter App!")

# Empty list
grades = []

# Get grades from user and add them to the list
grades.append(int(input("\nEnter your first grade (0 - 100): ")))
grades.append(int(input("Enter your second grade (0 - 100): ")))
grades.append(int(input("Enter your third grade (0 - 100): ")))
grades.append(int(input("Enter your fourth grade (0 - 100): ")))

# Show the submitted grades
print(f"\nYour grades are: {grades}")

# Order grades permanently from highest to lowest
grades.sort(reverse=True)

# Show result
print(f"\nYour grades from highest to lowest are: {grades}")

print("\nThe lowest two grades will now be dropped")

# Remove lowest grades from the list
dropped_1 = grades.pop()
dropped_2 = grades.pop()

# Show removed grades
print(f"\nRemoved grade: {dropped_1}")
print(f"Removed grade: {dropped_2}")

# Show remaining grades and highest grade
print(f"\nYour remaining grades are: {grades}")
print(f"Nice work! Your highest grade is {grades[0]}.")

