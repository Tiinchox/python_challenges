import random

print("------------------------Power-Ball Simulator------------------------")

# Get white balls and red ball from user
white_balls = int(input("\nHow many white balls to draw from the 5 winning numbers? (normally 69): "))
if white_balls < 5:
    white_balls = 5
red_balls = int(input("How many red balls to draw from for the Power-Ball? (normally 26): "))
if red_balls < 1:
    red_balls = 1

# Calculate odds
odds = 1
for i in range(5):
    odds *= white_balls - i

odds *= red_balls/120

# Get ticket interval from user
print(f"You have a 1 in {odds} chance of winning this lotery.")
ticket_interval = int(input("Purchase tickets in what interval? "))

# Empty list
winning_numbers = []

# Create winning ticket (white ball)
while len(winning_numbers) < 5:
    random_white = random.randint(1,white_balls)
    if random_white not in winning_numbers:
        winning_numbers.append(random_white)

# Sort ticket
winning_numbers.sort()

# Create winning ticket (red ball)
random_red = random.randint(1,red_balls)
winning_numbers.append(random_red)

# Simulate lottery
print("\n------------------------Welcome to the Power-Ball!------------------------")
print("Tonight's winning numbers are:", end=" ")
for num in winning_numbers:
    print(num,end=" ")

# Prompt the user to buy tickets
input("\nPress 'Enter' to start buying tickets! ")
tickets_purchased = 0
active = True
tickets_sold = []

# The lottery ends if the user gets a winner ticket or gives up
while winning_numbers not in tickets_sold and active == True:
    
    lottery_numbers = []

    # Create ticket (white ball)
    while len(lottery_numbers) < 5:
        random_white = random.randint(1,white_balls)
        if random_white not in lottery_numbers:
            lottery_numbers.append(random_white)

    # Sort ticket
    lottery_numbers.sort()

    # Create ticket (red ball)
    random_red = random.randint(1,red_balls)
    lottery_numbers.append(random_red)

    # Check the generated ticket is not in the ticket sold list
    if lottery_numbers not in tickets_sold:
        tickets_sold.append(lottery_numbers)
        tickets_purchased +=1        
        # Print it
        print(lottery_numbers)

    # If its in the list print a message    
    else:
        print("Losing ticket generated, disregard... :c")

    # Check if the user wants to continue buying tickets
    if tickets_purchased % ticket_interval == 0:
        print(f"\nSo far you bought {len(tickets_sold)} tickets with no winners.")
        choice = input("Would you like to buy more tickets? (y/n) ").lower()
        if choice != "y":
            active = False

# The user has the winning numbers
if lottery_numbers == winning_numbers:
    print("\nCongratulations, you won the Power-Ball! :D")
    print("Winning numbers:", end=" ")
    for num in lottery_numbers:
        print(num,end=" ")
    print(f"Purchased a total of {len(tickets_sold)}")    

# The user doesnt have the winning numbers
else:
    print(f"\nPurchased a total of {len(tickets_sold)} but neither was a winning ticket...")
    print("Better luck next time!")  


