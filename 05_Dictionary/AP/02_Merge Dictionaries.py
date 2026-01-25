"""
# Description of the Task
In this task, you will create two dictionaries and merge them into a single dictionary. 
After merging, you will print the merged dictionary.

# Instructions
Create two dictionaries with some predefined key-value pairs.
Merge these dictionaries into a single dictionary.
Print the merged dictionary.

# Learning Objective
The objective of this task is to learn how to merge two dictionaries in Python and understand the behavior of key-value pairs when merging.

# Sample Usage
Suppose we have two dictionaries:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
After merging, the resulting dictionary should be:
{'a': 1, 'b': 3, 'c': 4}
"""

print("=" * 80)
print("DICTIONARY MERGING TASK")
print("=" * 80)

# Step 1: Create two dictionaries with predefined key-value pairs
print("\nSTEP 1: Creating Two Dictionaries")
print("-" * 80)

dict1 = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

dict2 = {
    "age": 26,  # This will override the age from dict1
    "country": "USA",
    "occupation": "Developer"
}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)


# Step 2: Merge dictionaries - Method 1 using .update()
print("\n" + "=" * 80)
print("METHOD 1: Merging using .update() method")
print("-" * 80)

# Create a copy of dict1 to preserve original
merged_dict_1 = dict1.copy()
merged_dict_1.update(dict2)

print("Merged Dictionary (using .update()):")
print(merged_dict_1)
print("\nNote: The 'age' value from dict2 (26) overrides dict1's value (25)")


# Step 3: Merge dictionaries - Method 2 using ** unpacking operator
print("\n" + "=" * 80)
print("METHOD 2: Merging using ** unpacking operator")
print("-" * 80)

merged_dict_2 = {**dict1, **dict2}

print("Merged Dictionary (using ** operator):")
print(merged_dict_2)


# Step 4: Merge dictionaries - Method 3 using | operator (Python 3.9+)
print("\n" + "=" * 80)
print("METHOD 3: Merging using | operator (Python 3.9+)")
print("-" * 80)

merged_dict_3 = dict1 | dict2

print("Merged Dictionary (using | operator):")
print(merged_dict_3)


# Additional Example: Merging with different key-value pairs
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLE: Sample from Task Description")
print("-" * 80)

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

print("Dictionary A:", dict_a)
print("Dictionary B:", dict_b)

merged = {**dict_a, **dict_b}
print("Merged Dictionary:", merged)
print("\nExplanation: Key 'b' appears in both, so dict_b's value (3) is used")


# Demonstrating all original dictionaries remain unchanged
print("\n" + "=" * 80)
print("VERIFICATION: Original Dictionaries Unchanged")
print("-" * 80)

print("Original dict1:", dict1)
print("Original dict2:", dict2)
print("These remain unchanged when using copy() or unpacking")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
