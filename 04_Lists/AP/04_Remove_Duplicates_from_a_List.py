# ============================================================
# AP 04: Remove Duplicates from a List
# ============================================================
# Description: Take a list of integers from user, remove
#              duplicates, and print the updated list.
# ============================================================

# Prompt user to enter integers separated by spaces
user_input = input("Enter a list of integers separated by spaces: ")

# Convert input string to a list of integers
numbers = list(map(int, user_input.split()))
print("Original List:", numbers)

# Method 1: Using set (does not preserve order)
unique_set = list(set(numbers))
print("Using set (order not preserved):", unique_set)

# Method 2: Preserving order using loop
unique_ordered = []
for num in numbers:
    if num not in unique_ordered:
        unique_ordered.append(num)
print("Preserving order:", unique_ordered)

# Method 3: Using dict.fromkeys() (preserves order in Python 3.7+)
unique_dict = list(dict.fromkeys(numbers))
print("Using dict.fromkeys():", unique_dict)
