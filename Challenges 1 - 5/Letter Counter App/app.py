# Welcome message
print("Welcome to the Letter Counter App!")

# Get user input their name
name = input("Please enter your name: ").title() # We want it to be capitalized in the first letter

# Say hello to the user
print(f"Hello, {name}!")
print("I will count the number of times a specific letter occurs in a message")

# Get user input a message and a letter
message = input("Enter a message: ").lower() 
letter = input("Enter the letter you want to look for: ").lower()

# Count the number of ocurrences of the given letter in the given message
letter_count = message.count(letter)

# Print the result
print(f"{name}, the letter {letter.upper()} repeats {letter_count} times in your message.")