# Welcome message
print("Welcome to the Multiplication / Exponent Table App!")

# Get name and number from user
name = input("Please enter your name: ")
number = float(input("Enter the number you would like to work with: "))

# Store the name and a message in a variable
message = name.title() + ", Math is cool!"

# Print Multiplication Table
print(f"\nMultiplication Table for {number}")

print(f"\n\t 1 * {number} = {round(1 * number, 4)}") # Round to 4 decimals
print(f"\t 2 * {number} = {round(2 * number, 4)}")
print(f"\t 3 * {number} = {round(3 * number, 4)}")
print(f"\t 4 * {number} = {round(4 * number, 4)}")
print(f"\t 5 * {number} = {round(5 * number, 4)}")
print(f"\t 6 * {number} = {round(6 * number, 4)}")
print(f"\t 7 * {number} = {round(7 * number, 4)}")
print(f"\t 8 * {number} = {round(8 * number, 4)}")
print(f"\t 9 * {number} = {round(9 * number, 4)}")

# Print Exponent Table
print(f"\nExponent Table for {number}")

print(f"\n\t {number} ** 1 = {round(number ** 1, 4)}")
print(f"\t {number} ** 2 = {round(number ** 2, 4)}")
print(f"\t {number} ** 3 = {round(number ** 3, 4)}")
print(f"\t {number} ** 4 = {round(number ** 4, 4)}")
print(f"\t {number} ** 5= {round(number ** 5, 4)}")
print(f"\t {number} ** 6= {round(number ** 6, 4)}")
print(f"\t {number} ** 7= {round(number ** 7, 4)}")
print(f"\t {number} ** 8= {round(number ** 8, 4)}")
print(f"\t {number} ** 9= {round(number ** 9, 4)}")

# Print the message with different formats
print(f"\n{message}")
print(f"\t{message.lower()}")
print(f"\t\t{message.title()}")
print(f"\t\t\t{message.upper()}")