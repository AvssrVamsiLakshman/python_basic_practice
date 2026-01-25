"""
# Description of the Task
Write a Python program that takes a number as input from the user and checks if it is divisible by 2, 3, or both using if-else statements.

# Instructions
Prompt the user to enter a number.
Check if the number is divisible by 2, 3, or both.
Print appropriate messages based on the divisibility.

# Learning Objective
The objective of this task is to practice using if-else statements for conditional checks
 and to understand the modulus operator (%) for determining divisibility.

# Sample Usage
Example 1:
Input: 6
Output: The number 6 is divisible by both 2 and 3.

Example 2:
Input: 4
Output: The number 4 is divisible by 2.

Example 3:
Input: 9
Output: The number 9 is divisible by 3.

Example 4:
Input: 7
Output: The number 7 is not divisible by 2 or 3.
"""

print("=" * 80)
print("DIVISIBILITY CHECKER PROGRAM")
print("=" * 80)

# Step 1: Prompt user to enter a number
print("\n")
number_input = input("Enter a number: ")

# Convert to integer and check divisibility
try:
    number = int(number_input)
    
    print("\n" + "-" * 80)
    
    # Step 2: Check divisibility by 2 and 3
    divisible_by_2 = (number % 2 == 0)
    divisible_by_3 = (number % 3 == 0)
    
    # Step 3: Print appropriate message
    if divisible_by_2 and divisible_by_3:
        print(f"The number {number} is divisible by both 2 and 3.")
    elif divisible_by_2:
        print(f"The number {number} is divisible by 2.")
    elif divisible_by_3:
        print(f"The number {number} is divisible by 3.")
    else:
        print(f"The number {number} is not divisible by 2 or 3.")
    
    # Additional information
    print("\nDivisibility details:")
    print(f"  {number} ÷ 2 = {number / 2} (Remainder: {number % 2})")
    print(f"  {number} ÷ 3 = {number / 3:.2f} (Remainder: {number % 3})")
    
except ValueError:
    print("Error: Please enter a valid integer")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test with multiple numbers
test_numbers = [6, 4, 9, 7, 12, 15, 8, 21, 10, 18]

print("\nDivisibility check for sample numbers:")

for num in test_numbers:
    div_2 = (num % 2 == 0)
    div_3 = (num % 3 == 0)
    
    if div_2 and div_3:
        result = "both 2 and 3"
    elif div_2:
        result = "2 only"
    elif div_3:
        result = "3 only"
    else:
        result = "neither 2 nor 3"
    
    print(f"  {num:3} → divisible by {result}")


# Extended divisibility checker
print("\n" + "=" * 80)
print("BONUS: Extended Divisibility Checker (2, 3, 5)")
print("=" * 80)

check_num = input("\nEnter a number for extended check: ")

try:
    num = int(check_num)
    
    div_2 = (num % 2 == 0)
    div_3 = (num % 3 == 0)
    div_5 = (num % 5 == 0)
    
    print(f"\nDivisibility analysis for {num}:")
    print(f"  Divisible by 2: {'Yes' if div_2 else 'No'}")
    print(f"  Divisible by 3: {'Yes' if div_3 else 'No'}")
    print(f"  Divisible by 5: {'Yes' if div_5 else 'No'}")
    
    # Special cases
    if div_2 and div_3 and div_5:
        print(f"\n✓ {num} is divisible by 2, 3, and 5 (divisible by 30)")
    elif div_2 and div_3:
        print(f"\n✓ {num} is divisible by 2 and 3 (divisible by 6)")
    elif div_3 and div_5:
        print(f"\n✓ {num} is divisible by 3 and 5 (divisible by 15)")
    elif div_2 and div_5:
        print(f"\n✓ {num} is divisible by 2 and 5 (divisible by 10)")
    
except ValueError:
    print("Error: Please enter a valid integer")


# Fizz Buzz game (related concept)
print("\n" + "=" * 80)
print("BONUS: FizzBuzz Game")
print("=" * 80)

print("\nFizzBuzz for numbers 1-20:")
print("(Fizz for multiples of 3, Buzz for multiples of 5)")

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"  {i:2} → FizzBuzz")
    elif i % 3 == 0:
        print(f"  {i:2} → Fizz")
    elif i % 5 == 0:
        print(f"  {i:2} → Buzz")
    else:
        print(f"  {i:2} → {i}")


# Finding all divisors
print("\n" + "=" * 80)
print("BONUS: Finding All Divisors")
print("=" * 80)

find_num = input("\nEnter a number to find all divisors: ")

try:
    n = int(find_num)
    
    if n > 0:
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        
        print(f"\nDivisors of {n}: {divisors}")
        print(f"Number of divisors: {len(divisors)}")
        
        # Check if prime
        if len(divisors) == 2:
            print(f"{n} is a prime number!")
        
    else:
        print("Please enter a positive integer")
        
except ValueError:
    print("Error: Please enter a valid integer")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
