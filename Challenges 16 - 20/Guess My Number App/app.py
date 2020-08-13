import random

# Welcome message
print("Welcome to the Guess My Number App!")

# Get name from user
name = input("Enter your name: ").title()

print(f"\nHello, {name}! I'm thinking of a number between 1 and 20, can you guess my number?")

# Get random number
number = random.randint(1, 20)

# The user has 5 guesses
for i in range(5):
    guess = int(input("\nTake a guess: "))
    if guess > number:
        print("Your guess is too high...")
    elif guess < number:
        print("Your guess is too low...")
    else: # If the guess is right we break the loop
        break

# Once the loop is over print results
if guess == number:
    print(f"Woah {name}! That was the number I was thinking of! And only took you {i + 1} guesses!")
else: 
    print(f"\nWhoops, Gameover! The number I was thinking of was {number}! ;P")
