# ============================================================
# Concept: List Methods - del
# Topic: Deleting an Entire List
# ============================================================
# Description: Using del to completely delete a list variable.
#              Accessing it after deletion raises a NameError.
# ============================================================

numbers = [1, 2, 3, 4, 5]

del numbers

print(numbers)
print("The list 'numbers' has been deleted.")

# output :
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 7, in <module>
# NameError: name 'numbers' is not defined
