# ============================================================
# Concept: Operator Precedence
# Topic: Order of Operations with Division
# ============================================================
# Description: Division has higher precedence than subtraction
#              and addition. Order: 5/5=1.0, 10-1.0=9.0, 9.0+3=12.0
#              Subtraction and addition are left-to-right.
# Precedence: / > - = +
# ============================================================

# Expression with division, subtraction and addition
result = 10 - 5 / 5 + 3  # 5/5=1.0, 10-1.0=9.0, 9.0+3=12.0

# Displaying the result
print(result)            # Output: 12.0
