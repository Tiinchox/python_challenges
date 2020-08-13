# Create a list with users
users = ["jsmith", "mvilanoba", "mscott", "jperalta", "troynabed"]

# Welcome message
print("Welcome to the Shipping Account Program!")

# Get username from user
username = input("\nEnter your username to login: ")

# If the username is in the list 
if username in users:
    # Welcome back user
    print(f"\nWelcome back {username}!")

    # Show shipping rates
    print("These are the current shipping prices:")
    print("\nShipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")

    # Get quantity from user
    quantity = int(input("\nHow many items would you like to ship? "))

    # Initialize two variables
    price = 0
    unit = 0

    # Check what price corresponds to the quantity input by the user
    if quantity > 0 and quantity < 100:
        unit = 5.10
        price = quantity * unit # total price
    elif quantity >= 100 and quantity < 500:
        unit = 5.00
        price = quantity * unit
    elif quantity >= 500 and quantity < 1000:
        unit = 4.95
        price = quantity * unit
    elif quantity >= 1000:
        unit = 4.80
        price = quantity * unit
    else:
        print("You must ship at least one item")

    # Round the price to 2 decimals
    price = round(price, 2)
    
    # Print result
    print(f"\nTo ship {quantity} items it will cost you ${price} at ${unit} per item.") 

    # Ask if the user want to submit the order
    submit = input("\nWould you like to place this order? (y/n) ")

    # Check user's answer
    if submit.startswith("y"):
        print(f"Processing order......... {quantity} items shipped!")   
    else:
        print("No order is being place at this time.") 

# If the username is not in the list print a message
else:
    print("Sorry, there's no account with that username!")   
        

