# Welcome message
print("Welcome to the Even Odd Number Sorter App")

# Flag
flag = True

while flag:

    # Get numbers from user
    numbers = input("\nEnter a string of numbers separated by comma (,): ")

    # Empty variables
    evens = []
    odds = []

    # Replace spaces and split string by commas
    numbers = numbers.replace(" ","")
    num_list = numbers.split(",")

    print("\n-------Result Summary-------")

    # Convert each str to int and check if its even or odd
    for num in num_list:
        num = int(num)
        if num % 2 == 0:
            evens.append(num)
            print(f"\t{num} is even!")
        else:
            odds.append(num)
            print(f"\t{num} is odd!")

    # Sort lists
    evens.sort()
    odds.sort()

    # Print summary
    print(f"\nThe following {len(evens)} numbers are even:")
    for even in evens:
        print(f"\t{even}")

    print(f"\nThe following {len(odds)} numbers are odd:")
    for odd in odds:
        print(f"\t{odd}")       

    # Ask if the user wants to run it again
    choice = input("\nRun again? (y/n): ")
    if choice != "y":
        flag = False

print("Thank you for using the Even Odd Number Sorter App!")        
