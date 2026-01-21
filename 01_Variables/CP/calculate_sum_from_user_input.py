# ============================================================
# Concept: input() Function & Type Conversion
# Topic: Calculate Sum from User Input
# ============================================================
# Description: input() always returns a string. To perform
#              arithmetic operations, convert string to integer
#              using int() function.
# ============================================================

# Taking two numbers as input (returns string)
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Converting string to integers and calculating sum
sum_result = int(num1) + int(num2)

# Displaying the sum
print("Sum:", sum_result)
