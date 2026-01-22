# ============================================================
# Concept: Modifying Nested Lists
# Topic: Nested List with Booleans and Strings
# ============================================================
# Description: Modifying boolean elements in a nested list
#              that contains booleans and strings.
# ============================================================

bool_string_list = [
    [True, False],
    ["yes", "no"]
]

print("Original List:")
print(bool_string_list)
# Output: [[True, False], ['yes', 'no']]

bool_string_list[0][1] = True

print("\nModified List:")
print(bool_string_list)
# Output: [[True, True], ['yes', 'no']]
