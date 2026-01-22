# ============================================================
# Concept: Modifying Nested Lists
# Topic: Nested List with Mixed Data Types
# ============================================================
# Description: Modifying elements in a nested list that
#              contains mixed data types.
# ============================================================

mixed_list = [
    [1, "hello"],
    [2.5, "world"]
]

print("Original List:")
print(mixed_list)
# Output: [[1, 'hello'], [2.5, 'world']]

mixed_list[1][0] = 10.5

print("\nModified List:")
print(mixed_list)
# Output: [[1, 'hello'], [10.5, 'world']]
