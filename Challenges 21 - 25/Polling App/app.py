# Welcome message
print("Welcome to the Yes / No Polling App!")

# Get topic, number of voters and a password from user
topic = input("\nWhat 'Yes'/'No' topic will be voted today? ")
voters = int(input("How many voters will you allow on the issue? "))
password = input("Enter a password for polling results: ")

# Empty yes / no variables
yes = 0
no = 0

# Empty dict for poll results
results = {}

# Loop time
for i in range(voters):
    
    #Ask name
    name = input("\nEnter your name: ").title()

    # If that person already voted then show a message
    if name in results.keys():
        print("Sorry, you have already voted.")

    # Show topic and get answer    
    else:
        print(f"Welcome, {name}! The topic for today is: {topic}")
        vote = input("What do you think? Yes or no? ").lower().strip()

        # Update yes / no variables
        if vote == "yes" or vote == "y":
            vote = "yes"
            yes += 1
        elif vote == "no" or vote == "n":
            vote = "no"
            no +=1

        # Register the vote but don't count it for the results    
        else:
            print("This was a yes or no question but... whatever...")

        # Add that person's name and vote to the dict
        results[name] = vote
        print(f"Your vote of '{results[name]}' has been registered. Thank you, {name}!")

# Show voters
print(f"\nThe following {len(results)} people voted.")
for key in results.keys():
    print(f"\t{key}")

# Empty variable for winner
winner = 0

# Update winner depending the yes and no votes
if yes > no:
    winner = "Yes"
elif yes < no:
    winner = "No"
else:
    winner = "Tie"    

print(f"\nOn the following topic: '{topic}'")

# If it's not a tie print the winner
if winner != "Tie":
    print(f"{winner} wins! {yes} votes to {no} votes!")

# If it's a tie print another message
else:
    print("It's a tie! Go to Toss App coin to decide the real winner :P")    

# Ask for password to show the database
admin = input("\nTo see the voting results enter your password: ")

# If coincides, print the dict
if admin == password:
    for key, value in results.items():
        print(f"Name: {key}\t\tVote: {value}")
    print("\nThank you for using the Polling App!")

# If not, show another message
else:
    print("Whoops, password is incorrect. You'll never know who vote what >:D")    