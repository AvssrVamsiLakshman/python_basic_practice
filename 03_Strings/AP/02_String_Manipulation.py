# ============================================================
# AP 02: String Manipulation
# ============================================================
# Description: Perform various string manipulations on user input.
#              - Print in uppercase
#              - Print in lowercase
#              - Print with title case
#              - Print in reverse order
# ============================================================

# Prompt the user to enter a string
user_string = input("Enter a string: ")

# Print the string in uppercase
print("Uppercase:", user_string.upper())

# Print the string in lowercase
print("Lowercase:", user_string.lower())

# Print the string with first letter of each word capitalized
print("Title Case:", user_string.title())

# Print the string in reverse order
print("Reversed:", user_string[::-1])
