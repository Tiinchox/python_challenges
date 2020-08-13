import random

# Welcome message
print("Welcome to the Toss Coin App!")

print("\nI'll toss a coin the number of times you want!")

# Get number of flips
times = int(input("How many times should I flip the coin? "))

# Ask the user if we should display all results
answer = input("Would you like to see each flip? (y/n) ").lower()

# Initialize empty variables for heads and tails
heads = 0
tails = 0

print("\nFlippin'!\n")

for i in range(times):
    # Simulate a coin toss with .randomint()
    coin_flip = random.randint(0,1)
    if coin_flip == 0:
        heads += 1
        if answer.startswith("y"): # If the user wanted to see each result we print the message
            print("\tHEADS")
    else:
        tails += 1
        if answer.startswith("y"):
            print("\tTAILS")
    if heads == tails: # For each time the number of heads and tails are equal we print a message
        print(f"At {i + 1} flips, the number of heads and tails were equal at {heads} each!")

# Results

print(f"\nResult of flipping a coin {times} times:")
print("\nSIDE\t\tCOUNT\t\tPERCENTAGE")
print("-----------------------------------------")

# Calculate heads and tails rate
h_rate = float(heads * 100 / times)
h_rate = round(h_rate, 2)
t_rate = float(tails * 100 / times)
t_rate = round(t_rate, 2)

# Show results
print(f"Heads\t\t{heads}/{times}\t\t{h_rate}%")
print(f"Tails\t\t{tails}/{times}\t\t{t_rate}%\n")



