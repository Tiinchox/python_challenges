# Welcome message
print("Welcome to the Favorite Teacher App!")

# Create empty list
fav_teachers = []

# Get teachers from user and add them to the list
teacher_a = input("\nEnter your favorite teacher: ").title()
fav_teachers.append(teacher_a)

teacher_b = input("Enter your second favorite teacher: ").title()
fav_teachers.append(teacher_b)

teacher_c = input("Enter your third favorite teacher: ").title()
fav_teachers.append(teacher_c)

teacher_d = input("Enter your fourth favorite teacher: ").title()
fav_teachers.append(teacher_d)

# Show teachers ordered by rank, alphabetically and reverse alphabetically
print(f"\nYour favorite teachers ranked are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(fav_teachers, reverse=True)}")

# Show top 2 teachers, next two and last favorite
print(f"\nYour top two favorite teachers are: {fav_teachers[0]} and {fav_teachers[1]}")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}")
print(f"Your last favorite teacher is: {fav_teachers[-1]}")

# Print total of teachers in the list
print(f"You have a total of {len(fav_teachers)} teachers.")

# Get new #1 favorite from user and add it to the list
new_fav = input(f"\nOops, {fav_teachers[0]} is no longer your first favorite teacher. Who is your new favorite teacher? ").title()
fav_teachers.insert(0, new_fav)

# Show new order
print(f"\nYour favorite teachers ranked are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(fav_teachers, reverse=True)}")

# Show new positions
print(f"\nYour top two favorite teachers are: {fav_teachers[0]} and {fav_teachers[1]}")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}")
print(f"Your last favorite teacher is: {fav_teachers[-1]}")
print(f"You have a total of {len(fav_teachers)} teachers.")

# Get a teacher no longer liked by the user and remove it from the list
del_fav = input("\nYou've decided you no longer like a teacher. Which one would you like to remove from the list? ").title()
fav_teachers.remove(del_fav)

# Show new order
print(f"\nYour favorite teachers ranked are: {fav_teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(fav_teachers)}")
print(f"Your favorite teachers in reverse alphabetical order are: {sorted(fav_teachers, reverse=True)}")

# Show new positions
print(f"\nYour top two favorite teachers are: {fav_teachers[0]} and {fav_teachers[1]}")
print(f"Your next two favorite teachers are: {fav_teachers[2]} and {fav_teachers[3]}")
print(f"Your last favorite teacher is: {fav_teachers[-1]}")
print(f"You have a total of {len(fav_teachers)} teachers.")




