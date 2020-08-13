# Welcome message
print("Welcome to the Voter Registration App!")

# Get name and age
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))

# Create a list with political parties
parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# If the user is old enough
if age >= 18:
    print(f"\nCongratulations {name}! You are old enough to register to vote!")

    # Show list of parties
    print("\nHere is a list of political parties to join:")
    for party in parties:
        print(f"\t-{party}")

    # Get vote from user    
    vote = input("\nWhat party would you like to join? ").title()
    
    # Print a message depending the chosen party
    if vote in parties:
        print(f"\nCongratulations {name}! You have joined the {vote} Party!")
        if vote == "Republican" or vote == "Democratic":
            print("That is a major party!")
        elif vote == "Independent":
            print("You are an independent person!")    
        else:
            print("That is not a major party.")
    else:
        print("That is not a given party")        

# If the user is not old enough                
else:
    print("\nSorry, you are not old enough to register to vote!\n")