# ============================================================
# AP 01: Anagram Checker
# ============================================================
# Description: Check if two strings are anagrams of each other.
#              An anagram uses all the original letters exactly once.
# ============================================================

# Take two string inputs from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Convert both strings to lowercase and remove spaces
str1_cleaned = string1.lower().replace(" ", "")
str2_cleaned = string2.lower().replace(" ", "")

# Sort the characters in both strings
str1_sorted = sorted(str1_cleaned)
str2_sorted = sorted(str2_cleaned)

# Check if the sorted strings are equal
if str1_sorted == str2_sorted:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
