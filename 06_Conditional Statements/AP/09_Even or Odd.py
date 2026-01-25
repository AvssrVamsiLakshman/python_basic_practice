"""
# Description of the Task
The goal of this task is to write a Python program that determines whether a number entered by the user is even or odd. This will help you practice basic input handling, conditionals, and modulo operations in Python.

# Instructions
Prompt the user to enter a number.
Read the input from the user.
Check if the number is even or odd using the modulo operator (%).
Print an appropriate message indicating whether the number is even or odd.

# Learning Objective
By completing this task, you will learn how to:
Accept user input in Python.
Convert input strings to integers.
Use conditional statements (if, else).
Use the modulo operator to determine the remainder of a division.
"""

print("=" * 80)
print("EVEN OR ODD CHECKER PROGRAM")
print("=" * 80)

# Step 1: Prompt user to enter a number
print("\n")
user_input = input("Enter a number: ")

# Step 2: Convert input to integer
try:
    number = int(user_input)
    
    print("\n" + "-" * 80)
    
    # Step 3: Check if number is even or odd using modulo operator
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
    
    # Additional information
    print(f"\nExplanation: {number} ÷ 2 = {number // 2} with remainder {number % 2}")
    
except ValueError:
    print("Error: Please enter a valid integer")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test with multiple numbers
test_numbers = [0, 1, 2, 3, 4, 5, 10, 15, 20, 27, 100, 101, -4, -7]

print("\nEven/Odd check for sample numbers:")

for num in test_numbers:
    if num % 2 == 0:
        status = "even"
    else:
        status = "odd"
    
    print(f"  {num:4} → {status}")


# Checking a range of numbers
print("\n" + "=" * 80)
print("BONUS: Even/Odd Count in a Range")
print("=" * 80)

start = input("\nEnter start of range: ")
end = input("Enter end of range: ")

try:
    start_num = int(start)
    end_num = int(end)
    
    even_count = 0
    odd_count = 0
    even_numbers = []
    odd_numbers = []
    
    for i in range(start_num, end_num + 1):
        if i % 2 == 0:
            even_count += 1
            even_numbers.append(i)
        else:
            odd_count += 1
            odd_numbers.append(i)
    
    print(f"\nRange: {start_num} to {end_num}")
    print(f"Even numbers: {even_count} → {even_numbers}")
    print(f"Odd numbers: {odd_count} → {odd_numbers}")
    
except ValueError:
    print("Error: Please enter valid integers")


# Sum of even and odd numbers
print("\n" + "=" * 80)
print("BONUS: Sum of Even and Odd Numbers")
print("=" * 80)

numbers_input = input("\nEnter numbers separated by spaces: ")

try:
    numbers = [int(x) for x in numbers_input.split()]
    
    even_sum = 0
    odd_sum = 0
    even_list = []
    odd_list = []
    
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            even_list.append(num)
        else:
            odd_sum += num
            odd_list.append(num)
    
    print("\nAnalysis:")
    print(f"Even numbers: {even_list}")
    print(f"Sum of even numbers: {even_sum}")
    print(f"Odd numbers: {odd_list}")
    print(f"Sum of odd numbers: {odd_sum}")
    print(f"Total sum: {even_sum + odd_sum}")
    
except ValueError:
    print("Error: Please enter valid integers separated by spaces")


# Pattern printing based on even/odd
print("\n" + "=" * 80)
print("BONUS: Pattern Printing")
print("=" * 80)

print("\nPrinting numbers 1-20 with even/odd labels:")

for i in range(1, 21):
    if i % 2 == 0:
        print(f"  {i:2} → Even {'*' * (i // 2)}")
    else:
        print(f"  {i:2} → Odd  {'#' * ((i + 1) // 2)}")


# Finding even/odd properties
print("\n" + "=" * 80)
print("BONUS: Number Properties Checker")
print("=" * 80)

check_num = input("\nEnter a number to check its properties: ")

try:
    n = int(check_num)
    
    print(f"\nProperties of {n}:")
    
    # Even or odd
    if n % 2 == 0:
        print(f"  • Even number")
    else:
        print(f"  • Odd number")
    
    # Positive, negative, or zero
    if n > 0:
        print(f"  • Positive")
    elif n < 0:
        print(f"  • Negative")
    else:
        print(f"  • Zero")
    
    # Divisibility by other numbers
    if n % 3 == 0:
        print(f"  • Divisible by 3")
    if n % 5 == 0:
        print(f"  • Divisible by 5")
    if n % 10 == 0:
        print(f"  • Divisible by 10")
    
    # Square or not
    import math
    sqrt = math.sqrt(abs(n))
    if sqrt == int(sqrt):
        print(f"  • Perfect square (√{n} = {int(sqrt)})")
    
except ValueError:
    print("Error: Please enter a valid integer")


# List comprehension to separate even and odd
print("\n" + "=" * 80)
print("BONUS: List Comprehension Method")
print("=" * 80)

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [x for x in sample_list if x % 2 == 0]
odds = [x for x in sample_list if x % 2 != 0]

print(f"\nOriginal list: {sample_list}")
print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
