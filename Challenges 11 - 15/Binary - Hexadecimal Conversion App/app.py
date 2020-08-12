# Welcome message
print("Welcome to the Binary/Hexadecimal Converter App!")

# Get max number from user
num = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))

# Create a list starting with 1 up to the number from the user
decimals = list(range(1,num + 1)) # Use + 1 or will not include the user's number

# Empty lists
binaries = []
hexadecimals = []

# Loop through decimals adding the corresponding values to the other lists
for decimal in decimals:
    binaries.append(bin(decimal))
    hexadecimals.append(hex(decimal))

print("\nGenerating list........ Complete!")

print("\nWe will proceed to show you a portion of each list.")

# Get start num and end num from user
start_num = int(input("What number would you like to start at? "))
end_num = int(input("Great! What number would you like to stop at? "))

# Show partial results
print(f"\nDecimal values from {start_num} to {end_num}:\n")

for decimal in decimals[start_num - 1:end_num]: # Use - 1 because in lists we start at index 0
    print(decimal)

print(f"\nBinary values from {start_num} to {end_num}:\n")

for binary in binaries[start_num - 1:end_num]:
    print(binary)

print(f"\nHexadecimal values from {start_num} to {end_num}:\n")

for hexadecimal in hexadecimals[start_num - 1:end_num]:
    print(hexadecimal) 

# Ask the user to press Enter to view the complete list
show_all = input(f"\nPress Enter to see all values from 1 to {num}.")

# Table Header
print("\nDecimal\t\tBinary\t\tHexadecimal")
print("----------------------------------------------------")

# Loop through all the lists at the same time and print the values
for decimal, binary, hexadecimal in zip(decimals, binaries, hexadecimals):
    print(f"{decimal}\t\t{binary}\t\t{hexadecimal}")






