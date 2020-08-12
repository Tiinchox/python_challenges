import math

# Welcome message
print("Welcome to the Factorial Calculator App!")

# Get number from user
number = int(input("What number would you like to compute the factorial of? "))

# Show mathematical relationship of a factorial
print(f"\n{number}! = ", end=" ")
for num in range(1, number + 1):
    print(num, end="*")

# Using the math library
fact = math.factorial(number)
print("\n\nHere is the result from the math library:", f"The factorial of {number} is {fact}!", sep="\n")

# Using own algorithm
fact = 1
for i in range(1, number + 1):
    fact *= i
print("\nHere is the result from my own algorithm: ", f"The factorial of {number} is {fact}!", sep="\n") 

# Summary
print(f"\nIt is shown twice that {number}! = {fact} (with excitement)")

    
