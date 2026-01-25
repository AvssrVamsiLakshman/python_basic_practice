print("=" * 80)
print("SECTION 1: PRINTING NUMBERS")
print("=" * 80)

# program 1 - printing numbers
# learned that we can print numbers directly, no quotes needed

print("\n--- Program 1: Printing Numbers ---")

# printing a whole number (integer)
print("Integer:", 25)       

# printing decimal number (float)
print("Float:", 3.14)       


# program 2 - printing variables
# variables r like boxes that store stuff

print("\n--- Program 2: Printing Variables ---")

# making variables to store my info
name = "Vamsi Lakshman"   # text goes in quotes
age = 21                   # numbers without quotes

# printing them out
print("Name:", name)    
print("Age:", age)      


print("\n" + "=" * 80)
print("SECTION 2: VARIABLES AND DATA TYPES")
print("=" * 80)

# program 3 - all four data types

print("\n--- Program 3: All Four Basic Data Types ---")

# string - for text (use quotes!)
name = "Vamsi Lakshman"

# integer - whole numbers
age = 21

# float - numbers with decimals
height = 5.9

# boolean - True or False (capital letters!)
is_student = True

# printing all with their types using type()
print("Name:", name, "- Type:", type(name))
print("Age:", age, "- Type:", type(age))
print("Height:", height, "- Type:", type(height))
print("Is Student:", is_student, "- Type:", type(is_student))


# program 4 - boolean values
# this was confusing at first but now i get it

print("\n--- Program 4: Boolean Values ---")

# booleans can only be True or False
is_it_sunny = True      
is_it_raining = False   

print("Is it sunny?", is_it_sunny)      
print("Is it raining?", is_it_raining)  


print("\n" + "=" * 80)
print("SECTION 3: CHANGING VARIABLES")
print("=" * 80)

# program 5 - reassigning variables
# we can change variable values anytime

print("\n--- Program 5: Reassigning Variables ---")

# first setting score to 50
score = 50
print("Initial score:", score)    

# changing it to 85
score = 85
print("Updated score:", score)    


# program 6 - same value to many variables
# shortcut to give same value to multiple variables

print("\n--- Program 6: Chained Assignment ---")

# all three get 100
x = y = z = 100

print("Value of x:", x)    
print("Value of y:", y)    
print("Value of z:", z)    


# program 7 - multiple assignments in one line
# this saves time!

print("\n--- Program 7: Multiple Assignments ---")

# assigning three values at once
name, age, city = "Vamsi", 21, "Hyderabad"

print("Name:", name)      
print("Age:", age)        
print("City:", city)      


print("\n" + "=" * 80)
print("SECTION 4: ARITHMETIC OPERATIONS")
print("=" * 80)

# program 8 - addition
# using + to add two numbers

print("\n--- Program 8: Addition ---")

a = 15
b = 25

# adding them
result = a + b

print("Sum:", result)    # should be 40


# program 9 - subtraction
# using - to subtract

print("\n--- Program 9: Subtraction ---")

a = 50
b = 20

result = a - b

print("Difference:", result)    # should be 30


# program 10 - multiplication
# using * to multiply

print("\n--- Program 10: Multiplication ---")

a = 7
b = 8

result = a * b

print("Product:", result)    # should be 56


# program 11 - division
# using / to divide
# note: division always gives float even if answer is whole number

print("\n--- Program 11: Division ---")

a = 100
b = 4

result = a / b

print("Quotient:", result)    # gives 25.0 not 25


print("\n" + "=" * 80)
print("SECTION 5: STRING OPERATIONS")
print("=" * 80)

# program 12 - joining strings
# we use + to join strings together

print("\n--- Program 12: String Concatenation ---")

greeting = "Hello"
name = "Vamsi"

# joining with space in between
message = greeting + " " + name + "!"

print(message)    # Hello Vamsi!


# program 13 - len() function
# counts how many characters in string

print("\n--- Program 13: String Length ---")

name = "Vamsi Lakshman"

# getting length (counts spaces too!)
length = len(name)

print("Length of name:", length)  # should be 14


# program 14 - empty string length
# empty string has 0 length obviously

print("\n--- Program 14: Empty String Length ---")

empty_string = ""

length = len(empty_string)

print("Length:", length)  # 0


# program 15 - string with space
# spaces count as characters!

print("\n--- Program 15: Length with Spaces ---")

word_with_space = "Hello World"

length = len(word_with_space)

print("Length:", length)  # 11 (the space counts)


# program 16 - sentence length
# len() counts everything including punctuation

print("\n--- Program 16: Sentence Length ---")

sentence = "This is a sample sentence."

length = len(sentence)

print("Length:", length)  # 27


print("\n" + "=" * 80)
print("SECTION 6: NAMING CONVENTIONS")
print("=" * 80)

# program 17 - snake_case

print("\n--- Program 17: snake_case (recommended) ---")

# using underscore to separate words
first_name = "Vamsi"
last_name = "Lakshman"

full_name = first_name + " " + last_name

print("Full Name:", full_name)    


# program 18 - camelCase

print("\n--- Program 18: camelCase ---")

# first word lowercase, others start with capital
firstName = "Vamsi"
lastName = "Lakshman"

fullName = firstName + " " + lastName

print("Full Name:", fullName)    


print("\n" + "=" * 80)
print("SECTION 7: USER INPUT")
print("=" * 80)

# program 19 - taking user name
# input() function gets input from user
# (commenting out so program runs without waiting)

print("\n--- Program 19: Taking User Input ---")
# name = input("Enter your name: ")
# print("Hello!")
# print(name)
print("(skipped - needs user input)")


# program 20 - taking age
# remember: input() always returns string!

print("\n--- Program 20: Age Input ---")
# age = input("Enter your age: ")
# print("Your age is:", age)
print("(skipped - needs user input)")


# program 21 - taking two numbers
# taking multiple inputs

print("\n--- Program 21: Two Numbers Input ---")
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# print("First:", num1)
# print("Second:", num2)
print("(skipped - needs user input)")


# program 22 - greeting program
# combining input and print

print("\n--- Program 22: Greeting ---")
# name = input("Enter name: ")
# print("Hello,", name, "! Welcome to Python.")
print("(skipped - needs user input)")


# program 23 - calculating sum from input
# important: need to convert string to int!

print("\n--- Program 23: Sum with Type Conversion ---")

# using example values instead of input
num1 = "10"
num2 = "20"

# converting strings to integers then adding
sum_result = int(num1) + int(num2)

print("Sum:", sum_result)    # 30


print("\n" + "=" * 80)
print("SECTION 8: TYPE CHECKING")
print("=" * 80)

# program 24 - checking input type
# input() always gives string

print("\n--- Program 24: Type of Input ---")

user_input = "123"  # simulating input

print("Value:", user_input)
print("Type:", type(user_input))    # always str


# program 25 - integer type
# checking type of integer variable

print("\n--- Program 25: Integer Type ---")

age = 25

print("Age:", age)
print("Type:", type(age))    # int


# program 26 - float type
# checking type of decimal number

print("\n--- Program 26: Float Type ---")

height = 5.9

print("Height:", height)
print("Type:", type(height))    # float


# program 27 - boolean type
# checking type of True/False

print("\n--- Program 27: Boolean Type ---")

is_student = True

print("Is Student:", is_student)
print("Type:", type(is_student))    # bool


# program 28 - string type
# checking type of text

print("\n--- Program 28: String Type ---")

name = "Vamsi Lakshman"

print("Name:", name)
print("Type:", type(name))    # str


print("\n" + "=" * 80)
print("SECTION 9: REAL WORLD EXAMPLES")
print("=" * 80)

# program 29 - personal information
# storing different types of data

print("\n--- Program 29: Personal Info ---")

name = "Vamsi Lakshman"   
age = 27                   
height = 5.9               

print("Name:", name)       
print("Age:", age)         
print("Height:", height)   


# program 30 - student marks
# storing marks in variables

print("\n--- Program 30: Student Marks ---")

math_marks = 85       
science_marks = 90    
english_marks = 78    

print("Math:", math_marks)         
print("Science:", science_marks)   
print("English:", english_marks)   


# program 31 - product details
# like for online shopping

print("\n--- Program 31: Product Details ---")

product_name = "Laptop"     
product_price = 999.99      
stock_quantity = 50         

print("Product:", product_name)     
print("Price:", product_price)      
print("Stock:", stock_quantity)     


# program 32 - weather info
# storing temperature and weather

print("\n--- Program 32: Weather Info ---")

temperature_celsius = 22.5      
weather_condition = "Sunny"     

print("Temperature:", temperature_celsius, "°C")   
print("Weather:", weather_condition)     


print("\n" + "=" * 80)
print("DONE! ALL 32 PROGRAMS COMPLETED")
print("=" * 80)
