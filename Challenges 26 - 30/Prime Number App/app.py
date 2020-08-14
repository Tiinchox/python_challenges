import time

# Welcome message
print("Welcome to the Prime Number App!")

flag = True

while flag:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to de determine all prime numbers within a set range.")

    # Get choice from user
    choice = int(input("Enter your choice 1 or 2: "))

    if choice == 1:

        # Get number to check if its prime (only divided by 1 and itself)
        number = int(input("\nEnter a number to determine if it's prime or not: "))

        # Assume the number is prime
        prime_status = True

        # If that number is divided by any other number then break the loop
        for num in range(2, number):
            if number % num == 0:

                # If its not prime change status
                prime_status = False
                break

        # Show result to the user
        if prime_status == True:
            print(f"{number} is prime!")
        else:
            print(f"{number} is not prime!")   

        # Ask if the user wants to run it again
        run_choice = input("\nRun again? (y/n): ")    
        if run_choice != "y":
            flag = False     

    elif choice == 2:

        # Get info from user
        base = int(input("\nEnter the lower bound of your range: "))
        top = int(input("Enter your upper bound of your range: ")) 
        
        # Empty list
        primes = []

        # Start time
        start_time = time.time()

        # Loop through the bounds given by the user
        for num in range(base, top + 1):

            # If the base is greater than 1 then assume its a prime number
            if num > 1:
                prime_status = True

                # Like before loop to see if that number is divided by anything other than 1 and itself
                for i in range(2,num):
                    if num % i == 0:
                        prime_status = False
                        break
            else:
                prime_status = False

            # If its prime then add it to the list
            if prime_status == True:
                primes.append(num)
        
        # End time
        end_time = time.time()

        # Calculate the time it took to run the program
        delta_time = round(end_time - start_time, 4)

        # Show results
        print(f"\nCalculations took a total of {delta_time} seconds.")
        print(f"The following numbers between {base} and {top} are primes:")
        enter = input("Press enter to continue.")
        for prime in primes:
            print(prime)

        run_choice = input("\nRun again? (y/n): ")    
        if run_choice != "y":
            flag = False

    # The user enters an invalid command
    else:
        print("That's not a valid command.")

print("\nThank you for using Prime Number App!")