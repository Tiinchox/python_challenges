# Welcome message
print("Welcome to Temperature Conversion App!")

# Get temperature in Fahrenheit from user
f_degrees = float(input("Enter temperature in degrees Fahrenheit: "))

# Convert to Celsius
c_degrees = round(((f_degrees - 32) * 5 / 9), 4) # Round to 4 decimals

# Convert to Kelvin
k_degrees = round(((f_degrees - 32) * 5 / 9 + 273.15), 4) # Round to 4 decimals

# Print results aligned
print(f"Degrees Fahrenheit:\t{f_degrees}")
print(f"Degrees Celsius:\t{c_degrees}")
print(f"Degrees Kelvin:\t\t{k_degrees}")