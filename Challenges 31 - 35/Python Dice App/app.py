import random

# Functions
def dice_sides(): # Select sides for dice
    sides = int(input("\nHow many sides would you like on your dice? "))
    return sides

def dice_number(): # Select number of rolls
    number = int(input("How many dices would you like to roll? "))
    return number

def roll_dice(sides,number): # Simulate rolls
    dice = []
    print(f"\nYou rolled {number} {sides} sided dice.")
    print("\n-----Results are as followed-----")
    for i in range(number):
        result = random.randint(1,sides)
        print(f"\t{result}")
        dice.append(result)
    
    return dice

def sum_dice(dice): # Sum dices
    total = sum(dice)
    print(f"The total value of your roll is {total}.")

def roll_again(): # Ask if want to roll again
    choice = input("\nRoll again? (y/n) ").lower()
    if choice != "y":
        roll = False
    else:
        roll = True
    return choice

# Main code
print("Welcome to the Python Dice App!")
roll = True

while roll:
    # Create dice 
    d_sides = dice_sides()
    d_number = dice_number()

    # Roll dice
    my_dice = roll_dice(d_sides,d_number)

    # Sum dice
    sum_dice(my_dice)

    # Roll again?
    rolling = roll_again()

print("\nThank you for using the Python Dice App!")