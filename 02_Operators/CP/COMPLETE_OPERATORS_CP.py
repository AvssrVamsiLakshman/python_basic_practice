print("=" * 80)
print("SECTION 1: BASIC ARITHMETIC OPERATORS")
print("=" * 80)

# program 1 - addition
# the + operator adds numbers together

print("\n--- Program 1: Addition (+) ---")

a = 10
b = 5

result = a + b

print(f"{a} + {b} = {result}")    # 10 + 5 = 15


# program 2 - subtraction  
# the - operator subtracts

print("\n--- Program 2: Subtraction (-) ---")

a = 10
b = 5

result = a - b

print(f"{a} - {b} = {result}")    # 10 - 5 = 5


# program 3 - multiplication
# the * operator multiplies

print("\n--- Program 3: Multiplication (*) ---")

a = 10
b = 5

result = a * b

print(f"{a} * {b} = {result}")    # 10 * 5 = 50


# program 4 - division
# the / operator divides
# important: always gives float!

print("\n--- Program 4: Division (/) ---")

a = 10
b = 5

result = a / b

print(f"{a} / {b} = {result}")    # 10 / 5 = 2.0 (not 2!)


# program 5 - floor division
# the // operator divides but removes decimal part
# rounds down to nearest whole number

print("\n--- Program 5: Floor Division (//) ---")

a = 10
b = 3

result = a // b

print(f"{a} // {b} = {result}")    # 10 // 3 = 3 (not 3.333...)


# program 6 - modulus (remainder)
# the % operator gives remainder after division

print("\n--- Program 6: Modulus (%) ---")

a = 10
b = 3

result = a % b

print(f"{a} % {b} = {result}")    # 10 % 3 = 1 (remainder)


# program 7 - exponentiation (power)
# the ** operator raises to power
# like 2^3 in math

print("\n--- Program 7: Exponentiation (**) ---")

a = 2
b = 3

result = a ** b

print(f"{a} ** {b} = {result}")    # 2 ** 3 = 8


print("\n" + "=" * 80)
print("SECTION 2: BODMAS / OPERATOR PRECEDENCE")
print("=" * 80)

# teacher explained BODMAS order:
# Brackets () - highest priority
# Orders (exponents **) 
# Division / and Multiplication *
# Addition + and Subtraction - - lowest priority

# program 8 - BODMAS example 1
# showing how order matters

print("\n--- Program 8: BODMAS Example 1 ---")

# without brackets
result1 = 2 + 3 * 4
print("2 + 3 * 4 =", result1)    # 14 (multiply first!)

# with brackets
result2 = (2 + 3) * 4
print("(2 + 3) * 4 =", result2)    # 20 (brackets first!)


# program 9 - BODMAS example 2
# more complex expression

print("\n--- Program 9: BODMAS Example 2 ---")

result = 10 + 5 * 2
print("10 + 5 * 2 =", result)    # 20 (not 30!)


# program 10 - BODMAS example 3
# testing different operations

print("\n--- Program 10: BODMAS Example 3 ---")

result = 20 - 3 * 4 + 2
print("20 - 3 * 4 + 2 =", result)    # 10


# program 11 - BODMAS example 4
# division and multiplication together

print("\n--- Program 11: BODMAS Example 4 ---")

result = 10 / 2 * 3
print("10 / 2 * 3 =", result)    # 15.0 (left to right!)


# program 12 - BODMAS example 5
# using exponents

print("\n--- Program 12: BODMAS Example 5 ---")

result = 2 ** 3 + 4
print("2 ** 3 + 4 =", result)    # 12 (power first!)


# program 13 - BODMAS example 6
# complex with brackets

print("\n--- Program 13: BODMAS Example 6 ---")

result = (10 + 5) / (3 - 1)
print("(10 + 5) / (3 - 1) =", result)    # 7.5


# program 14 - BODMAS example 7
# all operators together

print("\n--- Program 14: BODMAS Example 7 ---")

result = 2 + 3 ** 2 * 4 - 5
print("2 + 3 ** 2 * 4 - 5 =", result)    # 33


# program 15 - BODMAS example 8
# nested brackets

print("\n--- Program 15: BODMAS Example 8 ---")

result = ((2 + 3) * 4) - 5
print("((2 + 3) * 4) - 5 =", result)    # 15


print("\n" + "=" * 80)
print("SECTION 3: COMPARISON OPERATORS")
print("=" * 80)

# these give True or False as answer
# used a lot in if statements later

# program 16 - greater than
# checks if left side bigger than right side

print("\n--- Program 16: Greater Than (>) ---")

a = 10
b = 5

result = a > b

print(f"{a} > {b} is {result}")    # True


# program 17 - less than
# checks if left side smaller than right side

print("\n--- Program 17: Less Than (<) ---")

a = 10
b = 5

result = a < b

print(f"{a} < {b} is {result}")    # False


# program 18 - equal to
# checks if both sides are same
# important: use == not = (that's assignment!)

print("\n--- Program 18: Equal To (==) ---")

a = 10
b = 10

result = a == b

print(f"{a} == {b} is {result}")    # True


# program 19 - not equal to
# checks if both sides are different

print("\n--- Program 19: Not Equal To (!=) ---")

a = 10
b = 5

result = a != b

print(f"{a} != {b} is {result}")    # True


# program 20 - greater than or equal to
# checks if left side is bigger OR same

print("\n--- Program 20: Greater Than or Equal (>=) ---")

a = 10
b = 10

result = a >= b

print(f"{a} >= {b} is {result}")    # True


# program 21 - less than or equal to
# checks if left side is smaller OR same

print("\n--- Program 21: Less Than or Equal (<=) ---")

a = 5
b = 10

result = a <= b

print(f"{a} <= {b} is {result}")    # True


print("\n" + "=" * 80)
print("SECTION 4: LOGICAL OPERATORS")
print("=" * 80)

# these combine multiple conditions
# and, or, not

# program 22 - AND operator
# both conditions must be True

print("\n--- Program 22: Logical AND ---")

a = 10
b = 5
c = 3

# checking if a > b AND a > c
result = (a > b) and (a > c)

print(f"({a} > {b}) and ({a} > {c}) is {result}")    # True (both are true)

result2 = (a > b) and (c > b)
print(f"({a} > {b}) and ({c} > {b}) is {result2}")    # False (second is false)


# program 23 - OR operator
# atleast one condition must be True
# think: condition1 OR condition2

print("\n--- Program 23: Logical OR ---")

a = 10
b = 5
c = 15

# checking if a > b OR a > c
result = (a > b) or (a > c)

print(f"({a} > {b}) or ({a} > {c}) is {result}")    # True (first is true)

result2 = (b > a) or (c > a)
print(f"({b} > {a}) or ({c} > {a}) is {result2}")    # True (second is true)


print("\n" + "=" * 80)
print("DONE! ALL 23 OPERATOR PROGRAMS COMPLETED")
print("=" * 80)
