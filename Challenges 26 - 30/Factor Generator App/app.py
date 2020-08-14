# Welcome message
print("Welcome to the Factor Generator App!")

# Set a flag
flag = True

while flag:
    factors = []

    # Get number from user
    number = int(input("\nEnter a number to determine all the factors of that number: "))

    # If number divided by num equals 0 add num to the factor list
    for num in range(1,number + 1):
        if number % num == 0:
            factors.append(num)

    # Print factors
    print(f"\nFactors of {number} are: ")
    for factor in factors:
        print(factor)

    # Show a summary    
    print("\nIn summary: ")
    for i in range(int(len(factors)/2)):
        print(f"{factors[i]}*{factors[-i - 1]}={number}")     

    # Ask if the user wants to run the program again
    choice = input("\nRun again? (y/n): ")
    
    # If not set flag to false and end loop
    if choice != "y":
        flag = False

print("\nThank you for using the Factor Generator App!")
