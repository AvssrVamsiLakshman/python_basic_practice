# ============================================================
# Concept: input() Function & type() Function
# Topic: Checking the Type of User Input
# ============================================================
# Description: The input() function ALWAYS returns a string,
#              regardless of what the user types (numbers, etc.).
#              Use type() to verify this behavior.
# ============================================================

# Taking any value as input
user_input = input("Enter any value: ")

# Displaying the input and its type
print("You entered:", user_input)
print("Type of input:", type(user_input))    # Always: <class 'str'>
