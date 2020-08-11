import datetime

# Create a list with two elements
grocery_list = ["Meat", "Cheese"]

# Create time variables
time = datetime.datetime.now()
month = time.month
day = time.day
hour = time.hour
minute = time.minute

# Print welcome message, date and list
print("Welcome to the Grocery List App!")
print(f"Current Date and Time: {day}/{month} {hour}:{minute}")
print(f"You currently have {grocery_list[0]} and {grocery_list[1]} in your grocery list.")

# Get three products from the user and add them to the list
grocery_list.append(input("\nEnter product to add to the grocery list: ").title())
grocery_list.append(input("Enter product to add to the grocery list: ").title())
grocery_list.append(input("Enter product to add to the grocery list: ").title())

# Show list and sorted list
print(f"\nHere is your grocery list: {grocery_list}")
grocery_list.sort()
print(f"Here is your grocery list sorted: {grocery_list}")

print("\nSimulating shopping...")

# Show number of items on the list and print it
print(f"\nCurrent grocery list: {len(grocery_list)} items.")
print(grocery_list)
# Prompt the user to enter a product and remove it from the list
prod_del_a = input("What product did you just buy? ").title()
print(f"Removing {prod_del_a} from the list.")
grocery_list.remove(prod_del_a)

# Repeat previous step 2 more times
print(f"\nCurrent grocery list: {len(grocery_list)} items.")
print(grocery_list)
prod_del_b = input("What product did you just buy? ").title()
print(f"Removing {prod_del_b} from the list.")
grocery_list.remove(prod_del_b)

print(f"\nCurrent grocery list: {len(grocery_list)} items.")
print(grocery_list)
prod_del_c = input("What product did you just buy? ").title()
print(f"Removing {prod_del_c} from the list.")
grocery_list.remove(prod_del_c)

# Show current list (should have only 2 elements now)
print(f"\nCurrent grocery list: {len(grocery_list)} items.")
print(grocery_list)

# Remove last item and print a message saying there is no stock of that product
no_stock = grocery_list.pop(-1)
print(f"\nSorry, the store is out of {no_stock}.")

# Prompt the user to enter another product and add it at the beginning of the list
grocery_list.insert(0, input("What product would you like to buy instead? ").title())

# Print final list
print(f"Here is what remains on your grocery list: {grocery_list}")


