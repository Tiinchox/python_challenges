# Welcome message
print("Welcome to the Basketball Roster App!")

# Create empty list
roster = []

# Get players from user and add them to the list
point_guard = input("\nChoose your point guard: ").title()
roster.append(point_guard)
shooting_guard = input("Choose your shooting guard: ").title()
roster.append(shooting_guard)
small_forward = input("Choose your small forward: ").title()
roster.append(small_forward)
power_forward = input("Choose your power forward: ").title()
roster.append(power_forward)
center = input("Choose your center: ").title()
roster.append(center)

# Show team composition
print("\n\tYour starting team for the upcoming season:")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall Forward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}")

# Remove Small Forward and get a substitute from the user
injured_player = roster.pop(2)
print(f"\nOh no, {injured_player} is injured!")
new_player = input(f"Who will take {injured_player} place? ").title()

# Add the substitute in the same position the injured player was
roster.insert(2, new_player)

# Show new team composition
print("\n\tYour starting team for the upcoming season:")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall Forward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t{roster[4]}")

# Wish good luck to the new player and show number of players 
print(f"\nGood luck {new_player}, you will do great!")
print(f"Your roster now has {len(roster)} players.")



