# ============================================================
# Concept: Operator Precedence
# Topic: Order of Operations with Mixed Types
# ============================================================
# Description: Mixing integers and floats in calculations.
#              Python automatically converts to float when needed.
#              Order: (3*2)=6, (4/2)=2.0, 7.5+6-2.0=11.5
# Note: Division always returns a float in Python 3.
# ============================================================

# Expression with mixed integer and float types
result = 7.5 + (3 * 2) - (4 / 2)  # 7.5+6-2.0=11.5

# Displaying the result
print(result)                      # Output: 11.5
