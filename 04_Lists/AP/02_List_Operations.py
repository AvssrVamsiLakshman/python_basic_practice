# ============================================================
# AP 02: List Operations
# ============================================================
# Description: Perform various operations on a list of numbers.
#              Find largest, smallest, sum, and reverse.
# ============================================================

# Create a list of numbers
numbers = [25, 67, 12, 89, 45, 34, 78, 56]

# Print the list
print("Original List:", numbers)

# Find and print the largest number
largest = max(numbers)
print("Largest Number:", largest)

# Find and print the smallest number
smallest = min(numbers)
print("Smallest Number:", smallest)

# Calculate and print the sum
total = sum(numbers)
print("Sum of all numbers:", total)

# Print the list in reverse order
reversed_list = numbers[::-1]
print("Reversed List:", reversed_list)

# Alternative: Using reverse() method
numbers_copy = numbers.copy()
numbers_copy.reverse()
print("Using reverse() method:", numbers_copy)
