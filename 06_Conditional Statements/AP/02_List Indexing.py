"""
# Description of the Task
Create a program that allows the user to access elements from a predefined list of colors based 
on the index provided by the user. 
The program should handle out-of-range indices gracefully by displaying an error message.

# Instructions
Define a list of colors.
Prompt the user to enter an index.
Print the color at the specified index.
If the index is out of range, print an error message.

# Learning Objective
Understanding how to define and work with lists in Python.
Practicing list indexing to access elements.
Implementing basic error handling for index out-of-range scenarios.
"""

print("=" * 80)
print("LIST INDEXING PROGRAM")
print("=" * 80)

# Step 1: Define a list of colors
colors = ["Red", "Green", "Blue", "Yellow", "Purple", "Orange", "Pink", "Brown"]

# Display the list with indices
print("\nAvailable colors:")
for i in range(len(colors)):
    print(f"  Index {i}: {colors[i]}")

# Step 2: Prompt user to enter an index
print("\n" + "-" * 80)
user_input = input(f"Enter an index (0 to {len(colors) - 1}): ")

# Convert input to integer
try:
    index = int(user_input)
    
    # Step 3: Check if index is in valid range
    print("-" * 80)
    
    if index >= 0 and index < len(colors):
        # Valid index - print the color
        print(f"Color at index {index}: {colors[index]}")
    elif index < 0 and abs(index) <= len(colors):
        # Negative index support
        print(f"Color at index {index}: {colors[index]}")
    else:
        # Out of range
        print("Error: Index out of range")
        
except ValueError:
    # Not a valid integer
    print("Error: Please enter a valid integer")


# Additional demonstration with multiple index attempts
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test various indices
test_indices = [0, 3, 7, 10, -1, -2]

for test_idx in test_indices:
    print(f"\nTrying index {test_idx}:")
    if test_idx >= 0 and test_idx < len(colors):
        print(f"  ✓ Color: {colors[test_idx]}")
    elif test_idx < 0 and abs(test_idx) <= len(colors):
        print(f"  ✓ Color: {colors[test_idx]}")
    else:
        print(f"  ✗ Error: Index out of range")


# Demonstrating safe access without error handling
print("\n" + "=" * 80)
print("BONUS: Using Conditional Check Before Access")
print("=" * 80)

def get_color_safe(color_list, idx):
    """Safely get color at index with bounds checking"""
    if 0 <= idx < len(color_list):
        return color_list[idx]
    elif -len(color_list) <= idx < 0:
        return color_list[idx]
    else:
        return "Index out of range"

# Test the safe function
print("\nUsing safe access function:")
print(f"Index 2: {get_color_safe(colors, 2)}")
print(f"Index 15: {get_color_safe(colors, 15)}")
print(f"Index -1: {get_color_safe(colors, -1)}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
