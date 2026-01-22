# ============================================================
# Concept: List Methods - del
# Topic: Deleting Elements from a Nested List
# ============================================================
# Description: Using del to remove an entire inner list
#              from a nested list.
# ============================================================

nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]

del nested_list[1]

print(nested_list)

# Output: [[1, 2, 3], [True, False]]
