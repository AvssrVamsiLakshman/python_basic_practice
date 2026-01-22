# ============================================================
# Concept: Modifying Nested Lists
# Topic: Modifying Nested Lists with Integers and Strings
# ============================================================
# Description: Changing elements in a nested list using
#              double indexing to access and modify values.
# ============================================================

data_list = [
    [10, 20, 30],
    ["apple", "banana", "cherry"],
    [1.1, 2.2, 3.3]
]

print("Original List:")
print(data_list)
# Output: [[10, 20, 30], ['apple', 'banana', 'cherry'], [1.1, 2.2, 3.3]]

data_list[0][2] = 99

data_list[1][1] = "blueberry"

print("\nModified List:")
print(data_list)
# Output: [[10, 20, 99], ['apple', 'blueberry', 'cherry'], [1.1, 2.2, 3.3]]
