# Welcome message
print("Welcome to the Database Admin Program!")

# Create dict with users and passwords
log_on_information = {
    "admin00":"admin1234",
    "mscott":"damnUtoby",
    "jperalta":"urS3xtape",
    "troyNabed":"dnd4thewin",
    "mvilanoba":"touman20"
}

# Get user from user
user = input("\nEnter your username: ")

# Check if it exist in the dict
if user in log_on_information.keys():
    # Get password from user
    password = input("Enter your password: ")
    # Check if it coincides with that user
    if password == log_on_information[user]:
        print(f"\nWelcome back, {user}! You are logged in!")
        # Check if user is the admin
        if user == "admin00":
            # Show complete database
            print("\nThis is the current database:")
            for key, values in log_on_information.items():
                print(f"Username: {key}\t\tPassword:{values}")
        else:
            # Ask if the user wants to change the password
            answer = input("\nWould you like to change your password? (y/n) ")
            if answer.startswith("y"):
                # Ask for new password with at least 8 characters
                print("Remember your password must have at least 8 characters.")
                new_pass = input("Enter your new password: ")
                # If less than the minimum do not change it and show the original password
                if len(new_pass) < 8:
                    print(f"Can't change password. '{new_pass}' is too short.")
                    print(f"\n{user}, your current password is {password}.")
                else:
                    # Change password and show new to user
                    print("\nPassword changed successfully!")
                    print(f"{user}, your current password is {new_pass}.")
            # If the user do not want to change it, show a message
            else:
                print("\nThank you for using the Database Admin Program. See you soon!")
    # The password does not coincide with the user
    else:
        print("\nInvalid username or password. Reload and try again!")
# The user does not exist in the dict        
else:
    print(f"\nThe user {user} is not registered in the database. Contact the admin to register it.")        


