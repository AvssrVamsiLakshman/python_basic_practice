# ============================================================
# Concept: Operator Precedence
# Topic: Complex Exponents
# ============================================================
# Description: Exponentiation (**) has higher precedence than
#              multiplication and addition. Order of evaluation:
#              2^3 = 8, then 8 * 3 = 24, then 5 + 24 = 29.
# Precedence: ** > * > +
# ============================================================

# Expression with exponent, multiplication and addition
result = 5 + 2 ** 3 * 3  # 2^3=8, 8*3=24, 5+24=29

# Displaying the result
print(result)            # Output: 29
