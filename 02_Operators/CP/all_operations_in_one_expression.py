# ============================================================
# Concept: Operator Precedence
# Topic: All Operations in One Expression
# ============================================================
# Description: Complex expression with all operations.
#              Order: (2+3)=5, (5-2)=3, 3^2=9, 5*9=45,
#              4/2=2.0, 45+2.0=47.0
# Precedence: () > ** > * = / > + = -
# ============================================================

# Expression combining all arithmetic operations
result = (2 + 3) * (5 - 2) ** 2 + 4 / 2  # 5*9+2.0=47.0

# Displaying the result
print(result)           # Output: 47.0
