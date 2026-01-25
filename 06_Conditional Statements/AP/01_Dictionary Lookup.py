"""
# Description of the Task
Create a program that initializes a dictionary with predefined key-value pairs. 
The program should then prompt the user to enter a key and search for this key in the dictionary. 
If the key exists, the program should print the corresponding value. If the key does not exist, 
the program should print an error message indicating that the key is not found.

# Instructions
Initialize a dictionary with some predefined key-value pairs.
Prompt the user to enter a key to search for in the dictionary.
Check if the key exists in the dictionary.
If the key exists, print the corresponding value.
If the key does not exist, print an error message.

# Learning Objective
This task aims to help beginners understand:
How to initialize and use dictionaries in Python.
How to access values using keys.
How to handle cases where a key does not exist in the dictionary.

# Sample Usage

Enter a key to search: apple
Value: A sweet red fruit
Enter a key to search: banana
Value: A long yellow fruit
Enter a key to search: pineapple
Error: Key not found in the dictionary
"""

print("=" * 80)
print("DICTIONARY LOOKUP PROGRAM")
print("=" * 80)

# Step 1: Initialize dictionary with predefined key-value pairs
fruit_dictionary = {
    "apple": "A sweet red fruit",
    "banana": "A long yellow fruit",
    "orange": "A citrus fruit with orange color",
    "grape": "Small round purple or green fruit",
    "mango": "A tropical fruit with sweet pulp",
    "strawberry": "A red berry with seeds on outside"
}

# Display available keys
print("\nAvailable fruits in dictionary:")
print(", ".join(fruit_dictionary.keys()))

# Step 2: Prompt user to enter a key
print("\n" + "-" * 80)
key_to_search = input("Enter a key to search: ")

# Step 3: Check if key exists and display result
print("-" * 80)

if key_to_search in fruit_dictionary:
    # Key exists - print the value
    print(f"Value: {fruit_dictionary[key_to_search]}")
else:
    # Key doesn't exist - print error message
    print("Error: Key not found in the dictionary")


# Additional demonstration with multiple searches
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Example searches
test_keys = ["apple", "banana", "pineapple", "grape"]

for test_key in test_keys:
    print(f"\nSearching for: {test_key}")
    if test_key in fruit_dictionary:
        print(f"✓ Found: {fruit_dictionary[test_key]}")
    else:
        print("✗ Error: Key not found in the dictionary")


# Alternative method using .get()
print("\n" + "=" * 80)
print("ALTERNATIVE METHOD: Using .get() method")
print("=" * 80)

search_key = input("\nEnter a key to search (using .get()): ")
result = fruit_dictionary.get(search_key, "Key not found in the dictionary")
print(f"Result: {result}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
