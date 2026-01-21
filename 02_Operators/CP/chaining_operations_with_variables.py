# ============================================================
# Concept: Operator Precedence
# Topic: Chaining Operations with Variables
# ============================================================
# Description: Complex expression using variables instead of
#              literal numbers. Order: (5+3)=8, (5*3)=15,
#              (5/3)=1.67, 8^2=64, 64-15+1.67=50.67
# Precedence: () > ** > * = / > + = -
# ============================================================

# Defining variables
x = 5                   # First variable
y = 3                   # Second variable

# Complex expression with multiple operations
result = (x + y) ** 2 - (x * y) + (x / y)

# Displaying the result
print(result)           # Output: 50.666666666666664
