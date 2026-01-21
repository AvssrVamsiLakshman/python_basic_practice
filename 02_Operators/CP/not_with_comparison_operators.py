# ============================================================
# Concept: Logical Operators
# Topic: NOT with Comparison Operators
# ============================================================
# Description: Using the 'not' operator to negate a condition.
#              'not' reverses the boolean value:
#              not True = False, not False = True.
# Syntax: result = not (condition)
# ============================================================

# Defining a variable
score = 60              # Student's score

# Using 'not' to negate the comparison result
is_failing = not (score >= 50)  # not True = False

# Displaying the result
print(is_failing)       # Output: False
