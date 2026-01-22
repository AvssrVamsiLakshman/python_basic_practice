# ============================================================
# Concept: List Methods - extend()
# Topic: Extending with a List of Mixed Data Types
# ============================================================
# Description: Using extend() to add multiple elements from
#              another list containing mixed data types.
# ============================================================

mixed_list = [1, "two", 3.0]
more_mixed = [False, "five", 6]

mixed_list.extend(more_mixed)
print(mixed_list)
# Output: [1, 'two', 3.0, False, 'five', 6]
