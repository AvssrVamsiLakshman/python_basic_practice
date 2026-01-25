print("=" * 80)
print("SECTION 1: BASIC IF STATEMENTS")
print("=" * 80)

# program 1 - checking if a number is equal
# using == (equality operator)
# if condition is True, code inside if block executes

print("\n--- Program 1: Checking if Number is Equal ---")

number = 100

if number == 100:
    print("The number is 100.")


# program 2 - checking if a string is "Hello"
# strings can also be compared with ==

print("\n--- Program 2: Checking if String is 'Hello' ---")

greeting = "Hello"

if greeting == "Hello":
    print("The greeting is Hello.")


# program 3 - checking if a number is greater than
# using > (greater than operator)

print("\n--- Program 3: Checking if Number is Greater Than ---")

number = 75

if number > 50:
    print("The number is greater than 50.")


# program 4 - check if temperature is above freezing
# practical example with greater than operator

print("\n--- Program 4: Check if Temperature is Above Freezing ---")

temperature = 10

if temperature > 0:
    print("The temperature is above freezing.")


print("\n" + "=" * 80)
print("SECTION 2: IF-ELSE STATEMENTS")
print("=" * 80)

# program 5 - checking if a number is even or odd
# using modulo operator (%)
# if condition False, else block executes

print("\n--- Program 5: Checking if Number is Even or Odd ---")

number = 8

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# program 6 - checking if a string contains "Python"
# using 'in' operator
# checks if substring exists in string

print("\n--- Program 6: Checking if String Contains 'Python' ---")

text = "I love Python."

if "Python" in text:
    print("The text contains 'Python'.")
else:
    print("The text does not contain 'Python'.")


# program 7 - checking if a person is eligible to vote
# using >= (greater than or equal to)

print("\n--- Program 7: Checking if Person is Eligible to Vote ---")

age = 20

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# program 8 - checking if temperature is hot or cold
# simple temperature check

print("\n--- Program 8: Checking if Temperature is Hot or Cold ---")

temperature = 30

if temperature > 25:
    print("It's hot outside.")
else:
    print("It's cold outside.")


print("\n" + "=" * 80)
print("SECTION 3: ELIF (ELSE-IF) STATEMENTS")
print("=" * 80)

# program 9 - checking temperature ranges
# multiple conditions with elif
# checks conditions in order from top to bottom

print("\n--- Program 9: Checking Temperature Ranges ---")

temperature = 22

if temperature < 0:
    print("It's freezing.")
elif temperature < 10:
    print("It's very cold.")
elif temperature < 20:
    print("It's cool.")
elif temperature < 30:
    print("It's warm.")
else:
    print("It's hot.")


# program 10 - checking user age for discounts
# practical ticket pricing example

print("\n--- Program 10: Checking User Age for Discounts ---")

age = 16

if age < 12:
    print("Child ticket: $10")
elif age < 18:
    print("Teen ticket: $15")
elif age < 65:
    print("Adult ticket: $20")
else:
    print("Senior ticket: $12")


# program 11 - check if number is small, medium, or large
# categorizing numbers into ranges

print("\n--- Program 11: Check if Number is Small, Medium, or Large ---")

number = 45

if number < 10:
    print("The number is small.")
elif number < 50:
    print("The number is medium.")
else:
    print("The number is large.")


# program 12 - check if number is positive, negative, or zero
# three-way number classification

print("\n--- Program 12: Check if Number is Positive, Negative, or Zero ---")

number = 5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


print("\n" + "=" * 80)
print("SECTION 4: NESTED IF STATEMENTS")
print("=" * 80)

# program 13 - checking for student scholarship eligibility
# nested if: if inside another if
# both outer and inner conditions must be True

print("\n--- Program 13: Checking for Student Scholarship Eligibility ---")

grade = 88
extra_curricular = True

if grade >= 85:
    if extra_curricular:
        print("Eligible for scholarship.")
    else:
        print("Not eligible for scholarship.")
else:
    print("Not eligible for scholarship (grade too low).")


# program 14 - checking a discount based on age and membership status
# nested if with multiple conditions

print("\n--- Program 14: Checking Discount Based on Age and Membership ---")

age = 30
is_member = False

if age >= 25:
    if is_member:
        print("Discount: 20%")
    else:
        print("Discount: 10%")
else:
    print("No discount.")


# program 15 - determining eligibility for a special event
# nested if with boolean conditions

print("\n--- Program 15: Determining Eligibility for Special Event ---")

is_weekend = True
has_invite = False

if is_weekend:
    if has_invite:
        print("You can attend the event.")
    else:
        print("You cannot attend the event (no invite).")
else:
    print("You cannot attend the event (not a weekend).")


# program 16 - checking for summer internship eligibility
# nested if with GPA and course completion

print("\n--- Program 16: Checking for Summer Internship Eligibility ---")

gpa = 3.5
completed_course = True

if gpa >= 3.0:
    if completed_course:
        print("Eligible for summer internship.")
    else:
        print("Not eligible for summer internship (course not completed).")
else:
    print("Not eligible for summer internship (GPA too low).")


print("\n" + "=" * 80)
print("SECTION 5: USING 'IS' OPERATOR")
print("=" * 80)

# program 17 - using is with lists
# 'is' checks if two variables refer to the same object in memory
# different from == which checks if values are equal

print("\n--- Program 17: Using 'is' with Lists ---")

a = [1, 2, 3]
b = a  # b points to same list as a

if a is b:
    print("a and b refer to the same object.")
else:
    print("a and b do not refer to the same object.")


# program 18 - comparing floats with is
# floats are different objects even if calculated to same value

print("\n--- Program 18: Comparing Floats ---")

f1 = 0.1 + 0.2
f2 = 0.3

if f1 is f2:
    print("Both 'f1' and 'f2' are the same object in memory.")
else:
    print("They are different objects in memory.")


# program 19 - using is with dictionaries
# two separate dictionaries are different objects

print("\n--- Program 19: Using 'is' with Dictionaries ---")

dict1 = {'name': 'Alice', 'age': 30}
dict2 = {'name': 'Alice', 'age': 30}

if dict1 is dict2:
    print("Both 'dict1' and 'dict2' are the same object in memory.")
else:
    print("They are different objects in memory.")


print("\n" + "=" * 80)
print("SECTION 6: USING 'IN' OPERATOR")
print("=" * 80)

# program 20 - using in with a dictionary
# checks if key exists in dictionary

print("\n--- Program 20: Using 'in' with a Dictionary ---")

my_dict = {'name': 'Alice', 'age': 30}

if 'age' in my_dict:
    print("Key 'age' is present in the dictionary.")
else:
    print("Key 'age' is not present in the dictionary.")


# program 21 - using in with a list containing integers and floats
# checks if value exists in list

print("\n--- Program 21: Using 'in' with List (Integers and Floats) ---")

numbers = [1, 2, 3.5, 4.5, 5]

if 3 in numbers:
    print("3 is in the list.")
else:
    print("3 is not in the list.")

if 3.5 in numbers:
    print("3.5 is in the list.")
else:
    print("3.5 is not in the list.")


# program 22 - using in with a string
# checks if substring exists in string

print("\n--- Program 22: Using 'in' with a String ---")

text = "Python is awesome"

if "Python" in text:
    print("'Python' is in the text.")
else:
    print("'Python' is not in the text.")


# program 23 - using in with a tuple
# checks if value exists in tuple

print("\n--- Program 23: Using 'in' with a Tuple ---")

colors = ("red", "green", "blue")

if "green" in colors:
    print("'green' is in the tuple.")
else:
    print("'green' is not in the tuple.")


print("\n" + "=" * 80)
print("SECTION 7: USING 'IS NOT' OPERATOR")
print("=" * 80)

# program 24 - using is not with list
# checks if two variables do NOT refer to same object

print("\n--- Program 24: Using 'is not' with List ---")

x = [4, 5, 6]
y = [4, 5, 6]  # different list object with same values

if x is not y:
    print("x and y are not the same object.")
else:
    print("x and y are the same object.")


# program 25 - using is not with dictionaries
# checks if dictionaries are different objects

print("\n--- Program 25: Using 'is not' with Dictionaries ---")

dict1 = {'name': 'Alice'}
dict2 = {'name': 'Bob'}

if dict1 is not dict2:
    print("dict1 and dict2 are different objects in memory.")
else:
    print("dict1 and dict2 refer to the same object in memory.")


# program 26 - using is not with None
# common use case: checking if variable is not None

print("\n--- Program 26: Using 'is not' with None ---")

value = "Hello"

if value is not None:
    print("Value is not None.")
else:
    print("Value is None.")


print("\n" + "=" * 80)
print("SECTION 8: USING 'NOT IN' OPERATOR")
print("=" * 80)

# program 27 - using not in with list
# checks if value does NOT exist in list

print("\n--- Program 27: Using 'not in' with List ---")

fruits = ["apple", "banana", "orange"]

if "grape" not in fruits:
    print("'grape' is not in the list.")
else:
    print("'grape' is in the list.")


# program 28 - using not in with dictionary
# checks if key does NOT exist in dictionary

print("\n--- Program 28: Using 'not in' with Dictionary ---")

student = {"name": "John", "age": 20}

if "grade" not in student:
    print("'grade' key is not in the dictionary.")
else:
    print("'grade' key is in the dictionary.")


# program 29 - using not in with string
# checks if substring does NOT exist

print("\n--- Program 29: Using 'not in' with String ---")

message = "Hello World"

if "Python" not in message:
    print("'Python' is not in the message.")
else:
    print("'Python' is in the message.")


print("\n" + "=" * 80)
print("SECTION 9: LOGICAL OPERATORS (AND, OR, NOT)")
print("=" * 80)

# program 30 - using AND operator
# both conditions must be True

print("\n--- Program 30: Using AND Operator ---")

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")


# program 31 - using OR operator
# at least one condition must be True

print("\n--- Program 31: Using OR Operator ---")

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax!")
else:
    print("It's a working day.")


# program 32 - using NOT operator
# reverses the boolean value

print("\n--- Program 32: Using NOT Operator ---")

is_raining = False

if not is_raining:
    print("You don't need an umbrella.")
else:
    print("You need an umbrella.")


# program 33 - combining AND and OR
# complex logical expressions

print("\n--- Program 33: Combining AND and OR ---")

age = 22
is_student = True
has_id = True

if (age >= 18 and age < 25) and (is_student or has_id):
    print("You get a discount.")
else:
    print("No discount available.")


print("\n" + "=" * 80)
print("SECTION 10: COMPARISON OPERATORS")
print("=" * 80)

# program 34 - less than (<)
# checks if left value is less than right value

print("\n--- Program 34: Less Than (<) ---")

a = 5
b = 10

if a < b:
    print(f"{a} is less than {b}.")


# program 35 - less than or equal to (<=)
# checks if left value is less than or equal to right value

print("\n--- Program 35: Less Than or Equal To (<=) ---")

score = 50
passing_score = 50

if score <= passing_score:
    print("Score is at or below the passing score.")


# program 36 - greater than or equal to (>=)
# checks if left value is greater than or equal to right value

print("\n--- Program 36: Greater Than or Equal To (>=) ---")

age = 21
legal_age = 21

if age >= legal_age:
    print("You are of legal age.")


# program 37 - not equal to (!=)
# checks if values are different

print("\n--- Program 37: Not Equal To (!=) ---")

password = "secret123"
user_input = "Secret123"

if user_input != password:
    print("Incorrect password.")
else:
    print("Correct password.")


print("\n" + "=" * 80)
print("SECTION 11: MULTIPLE CONDITIONS WITH ELIF")
print("=" * 80)

# program 38 - grade classification
# multiple ranges with elif

print("\n--- Program 38: Grade Classification ---")

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# program 39 - day of week
# string comparison with elif

print("\n--- Program 39: Day of Week ---")

day = "Monday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
elif day == "Friday":
    print("Almost the weekend!")
else:
    print("It's a weekday.")


# program 40 - BMI classification
# health-related categorization

print("\n--- Program 40: BMI Classification ---")

bmi = 22.5

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


print("\n" + "=" * 80)
print("SECTION 12: NESTED CONDITIONS WITH MULTIPLE LEVELS")
print("=" * 80)

# program 41 - loan approval system
# multiple nested conditions

print("\n--- Program 41: Loan Approval System ---")

credit_score = 720
income = 60000
has_collateral = True

if credit_score >= 700:
    if income >= 50000:
        if has_collateral:
            print("Loan approved with best rate.")
        else:
            print("Loan approved with standard rate.")
    else:
        print("Loan denied: Insufficient income.")
else:
    print("Loan denied: Low credit score.")


# program 42 - movie ticket pricing
# age-based pricing with additional checks

print("\n--- Program 42: Movie Ticket Pricing ---")

age = 8
is_3d = True

if age < 12:
    if is_3d:
        print("Child 3D ticket: $12")
    else:
        print("Child ticket: $8")
elif age < 65:
    if is_3d:
        print("Adult 3D ticket: $18")
    else:
        print("Adult ticket: $15")
else:
    if is_3d:
        print("Senior 3D ticket: $14")
    else:
        print("Senior ticket: $10")


print("\n" + "=" * 80)
print("SECTION 13: PRACTICAL APPLICATIONS")
print("=" * 80)

# program 43 - leap year checker
# complex condition with multiple checks

print("\n--- Program 43: Leap Year Checker ---")

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# program 44 - triangle validity checker
# mathematical condition checking

print("\n--- Program 44: Triangle Validity Checker ---")

side1 = 3
side2 = 4
side3 = 5

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("Valid triangle")
else:
    print("Invalid triangle")


# program 45 - time of day greeting
# hour-based greeting

print("\n--- Program 45: Time of Day Greeting ---")

hour = 14

if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")


# program 46 - season checker
# month-based season determination

print("\n--- Program 46: Season Checker ---")

month = 7

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Fall")


# program 47 - vowel or consonant checker
# character classification

print("\n--- Program 47: Vowel or Consonant Checker ---")

letter = "e"

if letter in "aeiouAEIOU":
    print(f"{letter} is a vowel.")
else:
    print(f"{letter} is a consonant.")


# program 48 - number sign checker
# positive, negative, or zero with additional info

print("\n--- Program 48: Number Sign Checker ---")

num = -15

if num > 0:
    print(f"{num} is positive.")
    if num % 2 == 0:
        print("It's also even.")
    else:
        print("It's also odd.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")


# program 49 - string length categorizer
# categorizing strings by length

print("\n--- Program 49: String Length Categorizer ---")

text = "Python"

if len(text) < 5:
    print("Short string")
elif len(text) <= 10:
    print("Medium string")
else:
    print("Long string")


# program 50 - divisibility checker
# checking divisibility by multiple numbers

print("\n--- Program 50: Divisibility Checker ---")

number = 15

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
elif number % 3 == 0:
    print(f"{number} is divisible by 3.")
elif number % 5 == 0:
    print(f"{number} is divisible by 5.")
else:
    print(f"{number} is not divisible by 3 or 5.")


print("\n" + "=" * 80)
print("END OF CONDITIONAL STATEMENTS CONCEPT PRACTICE")
print("=" * 80)
