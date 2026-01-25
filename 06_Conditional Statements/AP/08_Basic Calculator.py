"""# Description of the Task
Create a simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.

# Instructions
Prompt the user to enter the first number.
Prompt the user to enter the second number.
Prompt the user to choose an operation (+, -, *, /).
Perform the chosen operation and display the result.
Handle cases where the user attempts to divide by zero by displaying an appropriate message.

# Learning Objective
This task aims to help beginners:
Understand how to take user input in Python.
Use basic arithmetic operators.
Implement conditional statements to perform different operations based on user input.
Handle exceptions such as division by zero.
Print output to the console.
"""

print("=" * 80)
print("BASIC CALCULATOR PROGRAM")
print("=" * 80)

# Display available operations
print("\nAvailable Operations:")
print("  + : Addition")
print("  - : Subtraction")
print("  * : Multiplication")
print("  / : Division")

# Step 1: Get first number
print("\n" + "-" * 80)
num1_input = input("Enter the first number: ")

# Step 2: Get second number
num2_input = input("Enter the second number: ")

# Step 3: Get operation
operation = input("Choose an operation (+, -, *, /): ")

# Convert inputs to numbers and perform calculation
try:
    num1 = float(num1_input)
    num2 = float(num2_input)
    
    print("\n" + "-" * 80)
    
    # Step 4: Perform the chosen operation
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} × {num2} = {result}")
    
    elif operation == "/":
        # Step 5: Handle division by zero
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {num1} ÷ {num2} = {result}")
    
    else:
        print("Error: Invalid operation. Please choose +, -, *, or /")
    
except ValueError:
    print("Error: Please enter valid numbers")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Pre-defined calculations
calculations = [
    (10, 5, "+"),
    (10, 5, "-"),
    (10, 5, "*"),
    (10, 5, "/"),
    (10, 0, "/"),  # Division by zero
    (7, 3, "/"),   # Division with decimal
]

print("\nSample calculations:")

for n1, n2, op in calculations:
    if op == "+":
        res = n1 + n2
        print(f"  {n1} + {n2} = {res}")
    elif op == "-":
        res = n1 - n2
        print(f"  {n1} - {n2} = {res}")
    elif op == "*":
        res = n1 * n2
        print(f"  {n1} × {n2} = {res}")
    elif op == "/":
        if n2 == 0:
            print(f"  {n1} ÷ {n2} = Error (Division by zero)")
        else:
            res = n1 / n2
            print(f"  {n1} ÷ {n2} = {res}")


# Enhanced calculator with more operations
print("\n" + "=" * 80)
print("BONUS: Enhanced Calculator with More Operations")
print("=" * 80)

print("\nAdditional Operations:")
print("  ** : Power (exponentiation)")
print("  // : Floor division")
print("  %  : Modulus (remainder)")

calc_num1 = input("\nEnter first number: ")
calc_num2 = input("Enter second number: ")
calc_op = input("Choose operation (+, -, *, /, **, //, %): ")

try:
    n1 = float(calc_num1)
    n2 = float(calc_num2)
    
    print("\n" + "-" * 40)
    
    if calc_op == "+":
        print(f"{n1} + {n2} = {n1 + n2}")
    elif calc_op == "-":
        print(f"{n1} - {n2} = {n1 - n2}")
    elif calc_op == "*":
        print(f"{n1} × {n2} = {n1 * n2}")
    elif calc_op == "/":
        if n2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{n1} ÷ {n2} = {n1 / n2}")
    elif calc_op == "**":
        print(f"{n1} ^ {n2} = {n1 ** n2}")
    elif calc_op == "//":
        if n2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{n1} // {n2} = {n1 // n2}")
    elif calc_op == "%":
        if n2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(f"{n1} % {n2} = {n1 % n2}")
    else:
        print("Error: Invalid operation")
    
except ValueError:
    print("Error: Please enter valid numbers")


# Calculator with multiple operations
print("\n" + "=" * 80)
print("BONUS: Continuous Calculator")
print("=" * 80)

print("\nPerform multiple calculations (type 'quit' to exit)")

while True:
    print("\n" + "-" * 40)
    user_input = input("Enter calculation (e.g., 5 + 3) or 'quit': ")
    
    if user_input.lower() == 'quit':
        print("Exiting calculator...")
        break
    
    # Parse the input
    parts = user_input.split()
    
    if len(parts) == 3:
        try:
            val1 = float(parts[0])
            operator = parts[1]
            val2 = float(parts[2])
            
            if operator == "+":
                print(f"Result: {val1 + val2}")
            elif operator == "-":
                print(f"Result: {val1 - val2}")
            elif operator == "*":
                print(f"Result: {val1 * val2}")
            elif operator == "/":
                if val2 == 0:
                    print("Error: Division by zero!")
                else:
                    print(f"Result: {val1 / val2}")
            else:
                print("Error: Invalid operator")
        
        except ValueError:
            print("Error: Invalid numbers")
    else:
        print("Error: Invalid format. Use: number operator number")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
