# Import math library so we can have access to square root - sqrt() -
import math

# Welcome message
print("Welcome to the Right Triangle Solver App!")

# Get the two sides of the triangle from user
side_a = float(input("Enter first side of the triangle: "))
side_b = float(input("Enter second side of the triangle: "))

# Calculate hypotenuse
side_c = round((math.sqrt(side_a**2 + side_b**2)),3) # Round to 3 decimals

# Calculate area of triangle 
area = round((side_a * side_b / 2), 3) # Round to 3 decimals

# Print results
print(f"For a triangle with sides of {side_a} and {side_b} the hypotenuse is {side_c}.")
print(f"For a triangle with sides of {side_a} and {side_b} the area is {area}.")