print("=" * 80)
print("SECTION 1: STRING LENGTH")
print("=" * 80)

# program 1 - basic len()
# len() counts characters in string

print("\n--- Program 1: Basic String Length ---")

text = "Hello, World!"
length = len(text)

print(f"Text: {text}")
print(f"Length: {length}")    # 13 (counts comma, space, exclamation!)


# program 2 - empty string
# empty string has 0 length obviously

print("\n--- Program 2: Empty String ---")

empty = ""
length = len(empty)

print(f"Text: '{empty}'")
print(f"Length: {length}")    # 0


# program 3 - single character
# even one character counts as length 1

print("\n--- Program 3: Single Character ---")

char = "a"
length = len(char)

print(f"Text: {char}")
print(f"Length: {length}")    # 1


print("\n" + "=" * 80)
print("SECTION 2: CASE CONVERSION")
print("=" * 80)

# program 4 - upper()
# converts everything to UPPERCASE

print("\n--- Program 4: upper() Method ---")

text = "hello world"
upper_text = text.upper()

print(f"Original: {text}")
print(f"Uppercase: {upper_text}")    # HELLO WORLD


# program 5 - lower()
# converts everything to lowercase

print("\n--- Program 5: lower() Method ---")

text = "HELLO WORLD"
lower_text = text.lower()

print(f"Original: {text}")
print(f"Lowercase: {lower_text}")    # hello world


# program 6 - title()
# makes First Letter Of Each Word Capital

print("\n--- Program 6: title() Method ---")

text = "hello world"
title_text = text.title()

print(f"Original: {text}")
print(f"Title Case: {title_text}")    # Hello World


# program 7 - capitalize()
# only first letter capital, rest lowercase

print("\n--- Program 7: capitalize() Method ---")

text = "hello world"
cap_text = text.capitalize()

print(f"Original: {text}")
print(f"Capitalized: {cap_text}")    # Hello world


# program 8 - swapcase()
# this was cool! flips upper to lower and vice versa

print("\n--- Program 8: swapcase() Method ---")

text = "Hello World"
swapped = text.swapcase()

print(f"Original: {text}")
print(f"Swapped: {swapped}")    # hELLO wORLD


print("\n" + "=" * 80)
print("SECTION 3: REMOVING WHITESPACE")
print("=" * 80)

# program 9 - strip()
# removes spaces from both ends
# super useful for user input!

print("\n--- Program 9: strip() Method ---")

text = "   hello   "
stripped = text.strip()

print(f"Original: '{text}'")
print(f"Stripped: '{stripped}'")    # 'hello'


# program 10 - lstrip()
# removes spaces only from left side

print("\n--- Program 10: lstrip() Method ---")

text = "   hello   "
left_stripped = text.lstrip()

print(f"Original: '{text}'")
print(f"Left Stripped: '{left_stripped}'")    # 'hello   '


# program 11 - rstrip()
# removes spaces only from right side

print("\n--- Program 11: rstrip() Method ---")

text = "   hello   "
right_stripped = text.rstrip()

print(f"Original: '{text}'")
print(f"Right Stripped: '{right_stripped}'")    # '   hello'


print("\n" + "=" * 80)
print("SECTION 4: FINDING AND COUNTING")
print("=" * 80)

# program 12 - find()
# finds position of substring
# returns -1 if not found (not error!)

print("\n--- Program 12: find() Method ---")

text = "Hello, World!"
position = text.find("World")

print(f"Text: {text}")
print(f"Position of 'World': {position}")    # 7


# program 13 - find() not found
# when substring doesn't exist

print("\n--- Program 13: find() Not Found ---")

text = "Hello, World!"
position = text.find("Python")

print(f"Text: {text}")
print(f"Position of 'Python': {position}")    # -1


# program 14 - index()
# like find() but gives error if not found
# i prefer find() because its safer

print("\n--- Program 14: index() Method ---")

text = "Hello, World!"
position = text.index("World")

print(f"Text: {text}")
print(f"Position of 'World': {position}")    # 7


# program 15 - count()
# counts how many times substring appears
# case sensitive!

print("\n--- Program 15: count() Method ---")

text = "hello hello hello"
count = text.count("hello")

print(f"Text: {text}")
print(f"Count of 'hello': {count}")    # 3


# program 16 - count() single character
# counting individual letters

print("\n--- Program 16: Count Single Character ---")

text = "Hello, World!"
count = text.count("l")

print(f"Text: {text}")
print(f"Count of 'l': {count}")    # 3


print("\n" + "=" * 80)
print("SECTION 5: CHECKING START AND END")
print("=" * 80)

# program 17 - startswith()
# checks if string starts with something
# returns True or False

print("\n--- Program 17: startswith() Method ---")

text = "Hello, World!"
result = text.startswith("Hello")

print(f"Text: {text}")
print(f"Starts with 'Hello': {result}")    # True


# program 18 - startswith() False case
# when it doesn't start with that

print("\n--- Program 18: startswith() False ---")

text = "Hello, World!"
result = text.startswith("World")

print(f"Text: {text}")
print(f"Starts with 'World': {result}")    # False


# program 19 - endswith()
# checks if string ends with something

print("\n--- Program 19: endswith() Method ---")

text = "Hello, World!"
result = text.endswith("World!")

print(f"Text: {text}")
print(f"Ends with 'World!': {result}")    # True


# program 20 - endswith() False case

print("\n--- Program 20: endswith() False ---")

text = "Hello, World!"
result = text.endswith("Hello")

print(f"Text: {text}")
print(f"Ends with 'Hello': {result}")    # False


print("\n" + "=" * 80)
print("SECTION 6: REPLACING TEXT")
print("=" * 80)

# program 21 - replace()
# replaces old text with new text

print("\n--- Program 21: replace() Basic ---")

text = "Hello, World!"
new_text = text.replace("World", "Python")

print(f"Original: {text}")
print(f"Replaced: {new_text}")    # Hello, Python!


# program 22 - replace() multiple occurrences
# replaces all occurrences by default

print("\n--- Program 22: Replace Multiple ---")

text = "hello hello hello"
new_text = text.replace("hello", "hi")

print(f"Original: {text}")
print(f"Replaced: {new_text}")    # hi hi hi


# program 23 - replace() with count
# can limit how many to replace

print("\n--- Program 23: Replace with Limit ---")

text = "hello hello hello"
new_text = text.replace("hello", "hi", 2)    # only first 2

print(f"Original: {text}")
print(f"Replaced: {new_text}")    # hi hi hello


print("\n" + "=" * 80)
print("SECTION 7: SPLITTING STRINGS")
print("=" * 80)

# program 24 - split()
# splits string into list
# default splits by space

print("\n--- Program 24: split() Default ---")

text = "Hello World Python"
words = text.split()

print(f"Original: {text}")
print(f"Split: {words}")    # ['Hello', 'World', 'Python']


# program 25 - split() with separator
# can split by any character

print("\n--- Program 25: split() with Separator ---")

text = "apple,banana,orange"
fruits = text.split(",")

print(f"Original: {text}")
print(f"Split: {fruits}")    # ['apple', 'banana', 'orange']


# program 26 - split() with maxsplit
# limit number of splits

print("\n--- Program 26: split() with Limit ---")

text = "one two three four"
words = text.split(" ", 2)    # split only twice

print(f"Original: {text}")
print(f"Split: {words}")    # ['one', 'two', 'three four']


# program 27 - rsplit()
# splits from right side
# difference shows with maxsplit

print("\n--- Program 27: rsplit() Method ---")

text = "one two three four"
words = text.rsplit(" ", 2)    # split from right

print(f"Original: {text}")
print(f"Right Split: {words}")    # ['one two', 'three', 'four']


# program 28 - splitlines()
# splits at line breaks
# useful for multiline text

print("\n--- Program 28: splitlines() Method ---")

text = "Line 1\nLine 2\nLine 3"
lines = text.splitlines()

print(f"Original: {text}")
print(f"Lines: {lines}")    # ['Line 1', 'Line 2', 'Line 3']


print("\n" + "=" * 80)
print("SECTION 8: JOINING STRINGS")
print("=" * 80)

# program 29 - join()
# opposite of split! joins list into string
# syntax is weird: separator.join(list)

print("\n--- Program 29: join() with Space ---")

words = ["Hello", "World", "Python"]
text = " ".join(words)

print(f"List: {words}")
print(f"Joined: {text}")    # Hello World Python


# program 30 - join() with comma
# joining with different separator

print("\n--- Program 30: join() with Comma ---")

fruits = ["apple", "banana", "orange"]
text = ", ".join(fruits)

print(f"List: {fruits}")
print(f"Joined: {text}")    # apple, banana, orange


# program 31 - join() with no separator
# joining directly without space

print("\n--- Program 31: join() No Separator ---")

letters = ["H", "e", "l", "l", "o"]
word = "".join(letters)

print(f"List: {letters}")
print(f"Joined: {word}")    # Hello


print("\n" + "=" * 80)
print("SECTION 9: CHECKING MEMBERSHIP")
print("=" * 80)

# program 32 - in operator
# checks if substring exists in string

print("\n--- Program 32: 'in' Operator ---")

text = "Hello, World!"
result = "World" in text

print(f"Text: {text}")
print(f"'World' in text: {result}")    # True


# program 33 - not in operator
# checks if substring doesn't exist

print("\n--- Program 33: 'not in' Operator ---")

text = "Hello, World!"
result = "Python" not in text

print(f"Text: {text}")
print(f"'Python' not in text: {result}")    # True


print("\n" + "=" * 80)
print("SECTION 10: STRING REPETITION")
print("=" * 80)

# program 34 - * operator
# repeats string multiple times
# this was fun to learn!

print("\n--- Program 34: String Repetition ---")

text = "Hello! "
repeated = text * 3

print(f"Original: {text}")
print(f"Repeated 3 times: {repeated}")    # Hello! Hello! Hello! 


# program 35 - repetition with symbols
# useful for making separators

print("\n--- Program 35: Symbol Repetition ---")

separator = "=" * 20

print(f"Separator: {separator}")    # ====================


print("\n" + "=" * 80)
print("SECTION 11: STRING FORMATTING")
print("=" * 80)

# program 36 - format() basic
# old way of inserting values into string

print("\n--- Program 36: format() Method ---")

name = "Vamsi"
age = 21

text = "My name is {} and I am {} years old.".format(name, age)

print(text)    # My name is Vamsi and I am 21 years old.


# program 37 - format() with positions
# can specify order using numbers

print("\n--- Program 37: format() with Positions ---")

text = "I like {0} and {1}.".format("Python", "JavaScript")

print(text)    # I like Python and JavaScript.


# program 38 - format() with names
# can use variable names for clarity

print("\n--- Program 38: format() with Names ---")

text = "My name is {name} and I am {age} years old.".format(name="Vamsi", age=21)

print(text)


print("\n" + "=" * 80)
print("SECTION 12: F-STRINGS (BEST WAY!)")
print("=" * 80)

# program 39 - f-string basic
# just put f before quotes and use {}

print("\n--- Program 39: f-string Basic ---")

name = "Vamsi"
age = 21

text = f"My name is {name} and I am {age} years old."

print(text)


# program 40 - f-string with expressions
# can do math inside {}!

print("\n--- Program 40: f-string with Expressions ---")

a = 10
b = 5

text = f"{a} + {b} = {a + b}"

print(text)    # 10 + 5 = 15


# program 41 - f-string with methods
# can call methods inside {}

print("\n--- Program 41: f-string with Methods ---")

name = "vamsi"

text = f"Hello, {name.upper()}!"

print(text)    # Hello, VAMSI!


# program 42 - f-string with formatting
# can format numbers with :.2f etc

print("\n--- Program 42: f-string with Decimal Places ---")

price = 19.9999

text = f"Price: ${price:.2f}"

print(text)    # Price: $20.00


print("\n" + "=" * 80)
print("SECTION 13: RAW STRINGS AND ESCAPE SEQUENCES")
print("=" * 80)

# program 43 - escape sequences
# special characters using backslash

print("\n--- Program 43: Escape Sequences ---")

# \n for new line
print("Line 1\nLine 2")

# \t for tab
print("Name:\tVamsi")

# \\ for backslash
print("Path: C:\\Users\\Vamsi")


# program 44 - raw strings
# r before quotes ignores escape sequences
# useful for file paths!

print("\n--- Program 44: Raw String ---")

normal = "C:\\Users\\Vamsi"
raw = r"C:\Users\Vamsi"

print(f"Normal: {normal}")
print(f"Raw: {raw}")    # both print same but raw is easier to write


# program 45 - triple quotes
# for multiline strings

print("\n--- Program 45: Triple Quotes ---")

poem = """Roses are red,
Violets are blue,
Python is awesome,
And so are you!"""

print(poem)


print("\n" + "=" * 80)
print("SECTION 14: CHECKING STRING CONTENT")
print("=" * 80)

# program 46 - isalpha()
# checks if all characters are letters

print("\n--- Program 46: isalpha() Method ---")

text1 = "Hello"
text2 = "Hello123"

print(f"'{text1}'.isalpha(): {text1.isalpha()}")    # True
print(f"'{text2}'.isalpha(): {text2.isalpha()}")    # False


# program 47 - isdigit()
# checks if all characters are numbers

print("\n--- Program 47: isdigit() Method ---")

text1 = "12345"
text2 = "123abc"

print(f"'{text1}'.isdigit(): {text1.isdigit()}")    # True
print(f"'{text2}'.isdigit(): {text2.isdigit()}")    # False


# program 48 - isalnum()
# checks if all characters are letters or numbers

print("\n--- Program 48: isalnum() Method ---")

text1 = "Hello123"
text2 = "Hello 123"    # has space!

print(f"'{text1}'.isalnum(): {text1.isalnum()}")    # True
print(f"'{text2}'.isalnum(): {text2.isalnum()}")    # False


# program 49 - isspace()
# checks if string is all whitespace

print("\n--- Program 49: isspace() Method ---")

text1 = "   "
text2 = "  a  "

print(f"'{text1}'.isspace(): {text1.isspace()}")    # True
print(f"'{text2}'.isspace(): {text2.isspace()}")    # False


# program 50 - islower()
# checks if all letters are lowercase

print("\n--- Program 50: islower() Method ---")

text1 = "hello"
text2 = "Hello"

print(f"'{text1}'.islower(): {text1.islower()}")    # True
print(f"'{text2}'.islower(): {text2.islower()}")    # False


# program 51 - isupper()
# checks if all letters are uppercase

print("\n--- Program 51: isupper() Method ---")

text1 = "HELLO"
text2 = "Hello"

print(f"'{text1}'.isupper(): {text1.isupper()}")    # True
print(f"'{text2}'.isupper(): {text2.isupper()}")    # False


# program 52 - istitle()
# checks if in title case (first letter of each word capital)

print("\n--- Program 52: istitle() Method ---")

text1 = "Hello World"
text2 = "Hello world"

print(f"'{text1}'.istitle(): {text1.istitle()}")    # True
print(f"'{text2}'.istitle(): {text2.istitle()}")    # False


print("\n" + "=" * 80)
print("SECTION 15: OTHER USEFUL METHODS")
print("=" * 80)

# program 53 - center()
# centers string by adding spaces

print("\n--- Program 53: center() Method ---")

text = "Python"
centered = text.center(20)

print(f"Original: '{text}'")
print(f"Centered: '{centered}'")    # adds spaces on both sides


# program 54 - zfill()
# pads with zeros on left
# useful for number formatting!

print("\n--- Program 54: zfill() Method ---")

number = "42"
padded = number.zfill(5)

print(f"Original: {number}")
print(f"Zero-filled: {padded}")    # 00042


print("\n" + "=" * 80)
print("DONE! ALL 54 STRING PROGRAMS COMPLETED")
print("=" * 80)
