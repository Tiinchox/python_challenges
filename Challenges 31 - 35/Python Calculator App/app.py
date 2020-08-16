# Functions

def add(number1, number2):
    result = number1 + number2
    result = round(result,4)
    print(f"The sum of {number1} and {number2} is {result}.")
    return f"{number1} + {number2} = {result}"

def substract(number1, number2):
    result = number1 - number2
    result = round(result,4)
    print(f"The differences of {number1} and {number2} is {result}.")
    return f"{number1} - {number2} = {result}"

def multiply(number1, number2):
    result = number1 * number2
    result = round(result,4)
    print(f"The product of {number1} and {number2} is {result}.")
    return f"{number1} + {number2} = {result}" 

def divide(number1, number2):
    if number2 != 0:
        result = number1 / number2
        result = round(result,4)
        print(f"The quotient of {number1} and {number2} is {result}.")
        return f"{number1} / {number2} = {result}" 
    else:
        print("You cannot divide by zero!")
        return "DIV_ERROR"

def exponent(number1, number2):
    result = number1 ** number2
    result = round(result,4)
    print(f"{number1} raised to the power of {number2} is {result}.")
    return f"{number1} ** {number2} = {result}"         

# Main code

print("Welcome to the Python Calculator App!")
history = []
flag = True

while flag: 
    number1 = float(input("\nEnter a number: "))
    number2 = float(input("Enter another number: "))
    operation = input("Enter an operation (addition, substraction, multiplication, division or exponentiation): ").lower()
    if operation.startswith("a") or operation == "+":
        res = add(number1,number2)
    elif operation.startswith("s") or operation == "-":
        res = substract(number1,number2)
    elif operation.startswith("m") or operation == "*":
        res = multiply(number1,number2)
    elif operation.startswith("d") or operation == "/":
        res = divide(number1,number2)
    elif operation.startswith("e") or operation == "**":
        res = exponent(number1,number2)
    else:
        res ="OPP_ERROR"

    history.append(res)

    choice = input("\nWould you like to run the program again? (y/n) ").lower()
    if choice != "y":
        print("\nCalculation Summary: ")
        print("--------------------------")
        for i in history:
            print(i)
        flag = False

print("\nThank you for using the Python Calculator App!")
