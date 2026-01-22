# ============================================================
# Concept: List Methods - extend()
# Topic: Extending with Another List
# ============================================================
# Description: Using extend() to merge two lists by adding
#              all elements from one list to another.
# ============================================================

even_numbers = [2, 4, 6]

odd_numbers = [1, 3, 5]

even_numbers.extend(odd_numbers)

print(even_numbers)  # Output: [2, 4, 6, 1, 3, 5]
