# Welcome message
print("Welcome to the Grade AVG Calculator App!")

# Get name from user
name = input("\nEnter your name: ").title()

# Get number of grades
total = int(input("How many grades would you like to enter? "))
print()

# Empty list
grades = []

# Get grades from user and add them to the list
for i in range(total):
    grade = int(input("Enter grade (0 - 100): "))
    grades.append(grade)

# Display grades highest to lowest
print("\nGrades Highest to Lowest:")
grades.sort(reverse=True)
for grade in grades:
    print(f"\t{grade}")

# Average
avg = sum(grades) / len(grades)
avg = round(avg, 2)   

# Summary
print(f"\n{name}'s Grade Summary:")
print(f"\tTotal number of grades: {len(grades)}")
print(f"\tHighest Grade: {grades[0]}")
print(f"\tLowest Grade: {grades[-1]}")
print(f"\tAverage: {avg}")

# Get desired average from user and calculate the next grade needed to get it
desired_avg = int(input("\nWhat is your desired average? "))
next_grade = (desired_avg * (len(grades) + 1)) - sum(grades)
next_grade = round(next_grade, 2)
print(f"\nGood luck {name}!", f"You will need to get a {next_grade} on your next assignment to earn a {desired_avg} average.", sep="\n")

# Make a copy of grades
grades_copy = grades[:]

print("\nLet's see what your average could have been if you did better or worse on an assignment.")

# Get a grade to delete and a grade to replace it
del_grade = int(input("What grade would you like to change? "))
new_grade = int(input(f"What grade would you like to change {del_grade} into? "))

# Remove the grade from the list and add the new one
grades_copy.remove(del_grade)
grades_copy.append(new_grade)

# Print new grades highest to lowest
print("\nNew Grades Highest to Lowest:")
grades_copy.sort(reverse=True)
for grade in grades_copy:
    print(f"\t{grade}")

# New AVG
new_avg = sum(grades_copy) / len(grades_copy)
new_avg = round(new_avg, 2)

# Print new summary    
print(f"\n{name}'s New Grade Summary:")
print(f"\tTotal number of grades: {len(grades_copy)}")
print(f"\tHighest Grade: {grades_copy[0]}")
print(f"\tLowest Grade: {grades_copy[-1]}")
print(f"\tAverage: {new_avg}")

# Store both average in a new list
avgs = [avg, new_avg]
diff = max(avgs) - min(avgs)
diff = round(diff, 2)

# Compare results
print(f"\nYour new average would be {new_avg} compared to your real average of {avg}!")
print(f"That is a change of {diff} points!")

# Show original grades
print("\nToo bad your original grades are still the same!")
print(grades)
print("You should ask for extra credit!")
