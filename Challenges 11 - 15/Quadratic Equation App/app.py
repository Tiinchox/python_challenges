import cmath

# Welcome message
print("Welcome to the Quadratic Equation Solver App!")

# Explanation message
print("\nA quadratic equation is of the form ax^2 + bx + c = 0.", "Your solutions can be real or complex numbers.", "A complex number has two parts: a + bj.", "a is the real portion while bj is the imaginary portion", sep="\n")

# Get number of equations from user
equations = int(input("How many equations would you like to solve today? "))

# Loop through the number of equations
for equation in range(1,equations + 1):
    print(f"\nSolving equation #{equation}", "----------------------------------", sep="\n")

    # Get values for a, b and c
    a = float(input("Enter value of a (coefficient of x^2): "))
    b = float(input("Enter value of b (coefficient of x): "))
    c = float(input("Enter value of c (coefficient): "))

    # Do the maths
    x1 = (-b + cmath.sqrt(b**2 - 4*a*c)) / 2 * a
    x2 = (-b - cmath.sqrt(b**2 - 4*a*c)) / 2 * a

    # Print results
    print(f"\nThe solutions to {a}^2 + {b}x + {c} are:", f"\nx1 = {x1}", f"x2 = {x2}",sep="\n")

# Once the loop is over say goodbye
print("Thank you for using the Quadratic Equation Solver App. See you soon!")

