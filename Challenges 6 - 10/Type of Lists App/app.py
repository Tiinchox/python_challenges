# Create lists of strings, integers, floats and lists
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [2.5, 72.43, 6.6, 42.05]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\t\tSummary Table")

# Print a summary of each variable/list
print(f"\nThe variable num_strings is a {type(num_strings)}.") # Type
print(f"It contains the elements: {num_strings}") # Elements of the list
print(f"The element {num_strings[0]} is a {type(num_strings[0])}.") # First item and type of that element

print(f"\nThe variable num_ints is a {type(num_ints)}.")
print(f"It contains the elements: {num_ints}")
print(f"The element {num_ints[0]} is a {type(num_ints[0])}.")

print(f"\nThe variable num_floats is a {type(num_floats)}.")
print(f"It contains the elements: {num_floats}")
print(f"The element {num_floats[0]} is a {type(num_floats[0])}.")

print(f"\nThe variable num_lists is a {type(num_lists)}.")
print(f"It contains the elements: {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}.")

# Permanently sort num_strings and num_ints
print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
print(f"Sorted num_strings: {num_strings}")
num_ints.sort()
print(f"Sorted num_ints: {num_ints}")

# Print statement explaining differences
print("\nStrings are sorted alphabetically while integers are sorted numerically!")
