# ============================================================
# Concept: Modifying Nested Lists
# Topic: Nested List with Strings
# ============================================================
# Description: Modifying string elements in a nested list
#              using double indexing.
# ============================================================

string_list = [
    ["cat", "dog", "bird"],
    ["fish", "horse", "lion"]
]

print("Original List:")
print(string_list)
# Output: [['cat', 'dog', 'bird'], ['fish', 'horse', 'lion']]

string_list[1][2] = "tiger"

print("\nModified List:")
print(string_list)
# Output: [['cat', 'dog', 'bird'], ['fish', 'horse', 'tiger']]
