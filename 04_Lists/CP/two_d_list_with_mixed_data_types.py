# ============================================================
# Concept: 2D Lists
# Topic: 2D List with Mixed Data Types
# ============================================================
# Description: A 2D list where each row contains different
#              data types. Accessing elements with double indexing.
# ============================================================

two_d_list_2 = [
    [1, "apple", 3.5],
    ["banana", 2.5, 10],
    [True, "grape", 7.5]
]

print(two_d_list_2[2])  # Output: [True, 'grape', 7.5]

print(two_d_list_2[2][0])  # Output: True
print(two_d_list_2[2][1])  # Output: grape
print(two_d_list_2[2][2])  # Output: 7.5
