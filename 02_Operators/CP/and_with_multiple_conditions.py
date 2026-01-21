    # ============================================================
# Concept: Logical Operators
# Topic: AND with Multiple Conditions
# ============================================================
# Description: Combining 'and' with 'not' operators.
#              Returns True if temperature > 65 AND it is
#              NOT raining. Demonstrates compound conditions.
# Syntax: result = condition1 and not condition2
# ============================================================

# Defining variables for weather conditions
temperature = 70        # Current temperature
is_raining = False      # Whether it is raining

# Using 'and' with 'not' to check multiple conditions
go_outside = temperature > 65 and not is_raining

# Displaying the result
print(go_outside)       # Output: True
