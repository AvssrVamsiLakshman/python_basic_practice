# ============================================================
# Concept: Logical Operators
# Topic: AND with Conditions
# ============================================================
# Description: Using the 'and' operator to combine conditions.
#              Returns True only if BOTH conditions are True.
#              Here: age >= 18 AND has_license must both be True.
# Syntax: result = condition1 and condition2
# ============================================================

# Defining variables for the conditions
age = 25                # Person's age
has_license = True      # Whether person has a license

# Using 'and' operator to check both conditions
can_drive = age >= 18 and has_license

# Displaying the result
print(can_drive)        # Output: True
