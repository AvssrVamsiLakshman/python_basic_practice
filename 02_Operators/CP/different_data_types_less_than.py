# ============================================================
# Concept: Comparison Operators
# Topic: Different Data Types (Less Than or Equal)
# ============================================================
# Description: Comparing different data types with <= operator.
#              Python cannot compare an integer with a string
#              directly, resulting in a TypeError.
# Note: Always ensure both operands are of the same type.
# ============================================================

# Defining an integer and a string
a = 5                   # Integer data type
b = "5"                 # String data type

# Comparing different data types (will cause TypeError)
result = (a <= b)
print(result)
# Output: TypeError (cannot compare int and str)
