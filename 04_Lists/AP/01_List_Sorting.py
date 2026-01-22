# ============================================================
# AP 01: List Sorting
# ============================================================
# Description: Create a list of integers and sort it in
#              ascending and descending order.
# ============================================================

# Define a list of integers
numbers = [45, 12, 78, 34, 56, 23, 89, 67]

print("Original List:", numbers)

# Sort in ascending order
ascending = sorted(numbers)
print("Ascending Order:", ascending)

# Sort in descending order
descending = sorted(numbers, reverse=True)
print("Descending Order:", descending)

# Using list method (modifies original list)
numbers_copy = numbers.copy()
numbers_copy.sort()
print("\nUsing sort() method (ascending):", numbers_copy)

numbers_copy.sort(reverse=True)
print("Using sort() method (descending):", numbers_copy)
