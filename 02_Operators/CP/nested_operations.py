# ============================================================
# Concept: Operator Precedence
# Topic: Nested Operations
# ============================================================
# Description: Nested parentheses are evaluated from innermost
#              to outermost. Order: (2*3)=6, (5+6)=11,
#              11^2=121, 121-4=117.
# Precedence: () innermost first > ** > -
# ============================================================

# Expression with nested parentheses and exponentiation
result = (5 + (2 * 3)) ** 2 - 4  # (2*3)=6, (5+6)=11, 11^2=121, 121-4=117

# Displaying the result
print(result)           # Output: 117
