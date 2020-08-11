# Welcome message
print("Welcome to the MPH to MPS App!")

# Get speed in meter per hour from user
mph_speed = float(input("Enter your speed in miles per hour: ")) # We want to accept decimal numbers

# Convert to meter per second 
mps_speed = round((mph_speed * 0.4474),2) # Round the number to 2 decimals

# Print the result
print(f"Your speed in meter per second is {mps_speed}.")