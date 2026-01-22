# ============================================================
# AP 03: List Comprehension
# ============================================================
# Description: Create a list of first 20 natural numbers and
#              generate squares using list comprehension.
# ============================================================

# Create a list of first 20 natural numbers
natural_numbers = list(range(1, 21))
print("First 20 Natural Numbers:", natural_numbers)

# Create a list of squares using list comprehension
squares = [x ** 2 for x in natural_numbers]
print("Squares of Natural Numbers:", squares)

# Additional examples of list comprehension
# Even numbers only
even_numbers = [x for x in natural_numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# Odd numbers only
odd_numbers = [x for x in natural_numbers if x % 2 != 0]
print("Odd Numbers:", odd_numbers)

# Cubes of first 10 numbers
cubes = [x ** 3 for x in range(1, 11)]
print("Cubes of 1-10:", cubes)
