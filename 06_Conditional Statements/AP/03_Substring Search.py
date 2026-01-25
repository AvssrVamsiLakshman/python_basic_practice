"""
# Description of the Task
Write a Python program that:
Takes two string inputs from the user: a main string and a substring.
Checks if the substring is present in the main string.
Prints the starting index of the substring if found, or a message indicating it is not found.

# Instructions
Prompt the user to enter the main string.
Prompt the user to enter the substring.
Use Python string methods to determine if the substring is present in the main string.
If the substring is found, print the starting index of the first occurrence of the substring.
If the substring is not found, print an appropriate message.

# Learning Objective
The objective of this task is to practice working with Python strings, 
particularly string searching methods like find() or index(). 
This task helps in understanding how to manipulate and search within strings.

# Sample Usage
Enter the main string: Hello, welcome to the world of Python!
Enter the substring: welcome
Output: The substring 'welcome' is found at index 7.
"""

print("=" * 80)
print("SUBSTRING SEARCH PROGRAM")
print("=" * 80)

# Step 1: Prompt user to enter the main string
print("\n")
main_string = input("Enter the main string: ")

# Step 2: Prompt user to enter the substring
substring = input("Enter the substring: ")

# Step 3: Search for substring in main string
print("\n" + "-" * 80)

# Method 1: Using find() - returns -1 if not found
index_position = main_string.find(substring)

if index_position != -1:
    # Substring found
    print(f"The substring '{substring}' is found at index {index_position}.")
else:
    # Substring not found
    print(f"The substring '{substring}' is not found in the main string.")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Example with predefined strings
example_string = "Hello, welcome to the world of Python!"
test_substrings = ["welcome", "Python", "world", "Java", "Hello"]

print(f"\nMain string: '{example_string}'")
print("\nSearching for multiple substrings:")

for sub in test_substrings:
    pos = example_string.find(sub)
    if pos != -1:
        print(f"  ✓ '{sub}' found at index {pos}")
    else:
        print(f"  ✗ '{sub}' not found")


# Using 'in' operator for membership check
print("\n" + "=" * 80)
print("ALTERNATIVE METHOD: Using 'in' operator")
print("=" * 80)

main_str = input("\nEnter the main string: ")
sub_str = input("Enter the substring: ")

if sub_str in main_str:
    # Found - now get the index
    idx = main_str.find(sub_str)
    print(f"✓ The substring '{sub_str}' is found at index {idx}.")
else:
    print(f"✗ The substring '{sub_str}' is not found in the main string.")


# Finding all occurrences
print("\n" + "=" * 80)
print("BONUS: Finding All Occurrences")
print("=" * 80)

text = "Python is great. Python is powerful. Python is versatile."
search_word = "Python"

print(f"\nText: '{text}'")
print(f"Searching for all occurrences of '{search_word}':")

start = 0
occurrences = []

while True:
    pos = text.find(search_word, start)
    if pos == -1:
        break
    occurrences.append(pos)
    start = pos + 1

if occurrences:
    print(f"Found {len(occurrences)} occurrence(s) at indices: {occurrences}")
else:
    print("Not found")


# Case-sensitive vs case-insensitive search
print("\n" + "=" * 80)
print("BONUS: Case-Sensitive vs Case-Insensitive Search")
print("=" * 80)

text = "Hello World"
search = "hello"

print(f"\nText: '{text}'")
print(f"Searching for: '{search}'")

# Case-sensitive search
if search in text:
    print(f"  Case-sensitive: Found at index {text.find(search)}")
else:
    print(f"  Case-sensitive: Not found")

# Case-insensitive search
if search.lower() in text.lower():
    print(f"  Case-insensitive: Found at index {text.lower().find(search.lower())}")
else:
    print(f"  Case-insensitive: Not found")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
