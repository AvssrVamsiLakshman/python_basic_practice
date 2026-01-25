print("=" * 80)
print("SECTION 1: CREATING BASIC DICTIONARIES")
print("=" * 80)

# program 1 - basic dictionary
# creating a dictionary with curly braces {}
# key: value pairs separated by commas

print("\n--- Program 1: Creating Basic Dictionary ---")

employee = {"name": "Sarah", "position": "Manager", "salary": 70000}

print("Dictionary:", employee)


# program 2 - empty dictionary
# two ways to create empty dictionary

print("\n--- Program 2: Empty Dictionary ---")

empty_dict = {}
print("Empty dict:", empty_dict)
print("Type:", type(empty_dict))


# program 3 - accessing values with keys
# using square brackets [] with key name

print("\n--- Program 3: Accessing Values with Keys ---")

product = {"name": "Laptop", "brand": "Dell", "price": 800}

print("Product:", product)
print("Name:", product["name"])      # Laptop
print("Brand:", product["brand"])    # Dell
print("Price:", product["price"])    # 800


# program 4 - using variables as keys to access values
# we can store keys in variables and use them

print("\n--- Program 4: Using Variables as Keys ---")

employee = {"name": "Sarah", "position": "Manager", "salary": 70000}

key = "salary"
print("Employee:", employee)
print(f"Using key variable '{key}':", employee[key])    # 70000


# program 5 - dictionary with non-string keys (integers)
# keys don't have to be strings - they can be integers, tuples, or any immutable type

print("\n--- Program 5: Dictionary with Integer Keys ---")

numbers_dict = {1: "one", 2: "two", 3: "three"}

print("Dictionary:", numbers_dict)
print("Key 1:", numbers_dict[1])    # one
print("Key 2:", numbers_dict[2])    # two


# program 6 - dictionary with mixed data types
# values can be different types: string, int, boolean

print("\n--- Program 6: Mixed Data Types ---")

person = {"name": "John", "age": 30, "is_employed": True}

print("Person:", person)
print("Name:", person["name"])              # John
print("Age:", person["age"])                # 30
print("Is Employed:", person["is_employed"]) # True


print("\n" + "=" * 80)
print("SECTION 2: DICTIONARY METHODS - items(), keys(), values()")
print("=" * 80)

# program 7 - .items() method with empty dictionary
# returns dict_items object (empty)

print("\n--- Program 7: .items() with Empty Dictionary ---")

empty_dict = {}
empty_items = empty_dict.items()

print("Items:", empty_items)    # dict_items([])


# program 8 - .items() method with basic dictionary
# returns key-value pairs as tuples

print("\n--- Program 8: .items() with Basic Dictionary ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
car_items = car.items()

print("Dictionary:", car)
print("Items:", car_items)
# dict_items([('brand', 'Toyota'), ('model', 'Camry'), ('year', 2021)])


# program 9 - .keys() method with empty dictionary
# returns dict_keys object (empty)

print("\n--- Program 9: .keys() with Empty Dictionary ---")

empty_dict = {}
empty_keys = empty_dict.keys()

print("Keys:", empty_keys)    # dict_keys([])


# program 10 - .keys() method with basic dictionary
# returns all keys from dictionary

print("\n--- Program 10: .keys() with Basic Dictionary ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
car_keys = car.keys()

print("Dictionary:", car)
print("Keys:", car_keys)    # dict_keys(['brand', 'model', 'year'])


# program 11 - .values() method with empty dictionary
# returns dict_values object (empty)

print("\n--- Program 11: .values() with Empty Dictionary ---")

empty_dict = {}
empty_values = empty_dict.values()

print("Values:", empty_values)    # dict_values([])


# program 12 - .values() method with basic dictionary
# returns all values from dictionary

print("\n--- Program 12: .values() with Basic Dictionary ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
car_values = car.values()

print("Dictionary:", car)
print("Values:", car_values)    # dict_values(['Toyota', 'Camry', 2021])


print("\n" + "=" * 80)
print("SECTION 3: ACCESSING VALUES SAFELY WITH .get() METHOD")
print("=" * 80)

# program 13 - .get() method with existing key
# safer way to access values
# doesn't raise error if key missing

print("\n--- Program 13: .get() with Existing Key ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

brand = car.get("brand")
print("Dictionary:", car)
print("Brand using .get():", brand)    # Toyota


# program 14 - .get() method with non-existing key and default value
# returns default value if key doesn't exist
# prevents KeyError

print("\n--- Program 14: .get() with Default Value ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

color = car.get("color", "Not Found")
print("Dictionary:", car)
print("Color:", color)    # Not Found


# program 15 - .get() method without default value
# returns None if key doesn't exist and no default provided

print("\n--- Program 15: .get() without Default Value ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

color = car.get("color")
print("Dictionary:", car)
print("Color:", color)    # None


print("\n" + "=" * 80)
print("SECTION 4: UPDATING AND MODIFYING DICTIONARIES")
print("=" * 80)

# program 16 - updating existing key values directly
# using assignment to change value

print("\n--- Program 16: Updating Values Directly ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

car["year"] = 2022
print("After update:", car)    # year changed to 2022


# program 17 - .update() method to update existing key values
# can update multiple keys at once

print("\n--- Program 17: .update() Method ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

car.update({"year": 2022})
print("After update:", car)    # {'brand': 'Toyota', 'model': 'Camry', 'year': 2022}


# program 18 - adding new key-value pairs
# assign value to new key

print("\n--- Program 18: Adding New Key-Value Pairs ---")

car = {"brand": "Toyota", "model": "Camry"}
print("Original:", car)

car["year"] = 2021
car["color"] = "blue"
print("After adding:", car)


# program 19 - .update() to add multiple key-value pairs
# more efficient for adding multiple items

print("\n--- Program 19: .update() to Add Multiple Pairs ---")

car = {"brand": "Toyota"}
print("Original:", car)

car.update({"model": "Camry", "year": 2021, "color": "blue"})
print("After update:", car)


print("\n" + "=" * 80)
print("SECTION 5: NESTED DICTIONARIES")
print("=" * 80)

# program 20 - creating simple nested dictionary
# dictionary inside another dictionary

print("\n--- Program 20: Simple Nested Dictionary ---")

student = {
    "name": "John",
    "details": {
        "age": 21,
        "grade": "A"
    }
}

print("Student:", student)


# program 21 - accessing nested values
# use multiple square brackets

print("\n--- Program 21: Accessing Nested Values ---")

student = {
    "name": "John",
    "details": {
        "age": 21,
        "grade": "A"
    }
}

age = student["details"]["age"]
print("Student:", student)
print("Age:", age)    # 21


# program 22 - modifying nested values
# access nested key and assign new value

print("\n--- Program 22: Modifying Nested Values ---")

student = {
    "name": "John",
    "details": {
        "age": 21,
        "grade": "A"
    }
}

print("Original:", student)
student["details"]["grade"] = "A+"
print("After update:", student)
# grade changed from 'A' to 'A+'


# program 23 - complex nested dictionary
# multiple levels of nesting with lists inside

print("\n--- Program 23: Complex Nested Dictionary ---")

employee = {
    "name": "Emma",
    "position": "Manager",
    "projects": {
        "current": ["Project A", "Project B"],
        "completed": ["Project X"]
    }
}

print("Employee:")
print(employee)


# program 24 - accessing values in complex nested dictionary
# navigating through multiple levels

print("\n--- Program 24: Accessing Complex Nested Values ---")

employee = {
    "name": "Emma",
    "position": "Manager",
    "projects": {
        "current": ["Project A", "Project B"],
        "completed": ["Project X"]
    }
}

current_projects = employee["projects"]["current"]
print("Current projects:", current_projects)    # ['Project A', 'Project B']


# program 25 - nested dictionary for classroom
# storing multiple students in one class

print("\n--- Program 25: Classroom Nested Dictionary ---")

classroom = {
    "class_name": "Physics",
    "students": {
        "student1": {"name": "Alice", "age": 20},
        "student2": {"name": "Bob", "age": 22}
    }
}

print("Classroom:")
print(classroom)


# program 26 - accessing nested value in classroom dictionary
# multiple levels deep

print("\n--- Program 26: Accessing Classroom Nested Values ---")

classroom = {
    "class_name": "Physics",
    "students": {
        "student1": {"name": "Alice", "age": 20},
        "student2": {"name": "Bob", "age": 22}
    }
}

student_name = classroom["students"]["student2"]["name"]
print("Student2 name:", student_name)    # Bob


# program 27 - modifying nested value in classroom dictionary
# change age of student1

print("\n--- Program 27: Modifying Classroom Nested Values ---")

classroom = {
    "class_name": "Physics",
    "students": {
        "student1": {"name": "Alice", "age": 20},
        "student2": {"name": "Bob", "age": 22}
    }
}

print("Original:")
print(classroom)

classroom["students"]["student1"]["age"] = 21

print("\nAfter update:")
print(classroom)


# program 28 - accessing nested dictionary values with .get()
# using .get() for safe nested access

print("\n--- Program 28: Nested Access with .get() ---")

student = {
    "name": "John",
    "grades": {
        "math": 90,
        "science": 85
    }
}

math_grade = student.get("grades").get("math")
print("Student:", student)
print("Math grade:", math_grade)    # 90


# program 29 - adding new key-value pair to nested dictionary
# adding to a list inside nested dict

print("\n--- Program 29: Adding to Nested Dictionary ---")

employee = {
    "name": "Emma",
    "position": "Manager",
    "projects": {
        "current": ["Project A", "Project B"],
        "completed": ["Project X"]
    }
}

print("Original:")
print(employee)

employee["projects"]["current"].append("Project C")

print("\nAfter adding Project C:")
print(employee)


print("\n" + "=" * 80)
print("SECTION 6: DELETING FROM DICTIONARIES")
print("=" * 80)

# program 30 - deleting key-value pair with del
# removes key and its value

print("\n--- Program 30: Deleting with del ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

del car["year"]
print("After deleting year:", car)    # {'brand': 'Toyota', 'model': 'Camry'}


# program 31 - .pop() method to remove and return value
# removes key and returns its value

print("\n--- Program 31: .pop() Method ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

removed_value = car.pop("year")
print("Removed value:", removed_value)    # 2021
print("After pop:", car)    # {'brand': 'Toyota', 'model': 'Camry'}


# program 32 - .pop() with default value
# returns default if key doesn't exist

print("\n--- Program 32: .pop() with Default ---")

car = {"brand": "Toyota", "model": "Camry"}
print("Original:", car)

color = car.pop("color", "Not Found")
print("Popped color:", color)    # Not Found
print("Dictionary:", car)


# program 33 - .popitem() method
# removes and returns last inserted key-value pair

print("\n--- Program 33: .popitem() Method ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

removed = car.popitem()
print("Removed item:", removed)    # ('year', 2021)
print("After popitem:", car)


# program 34 - .clear() method
# removes all items from dictionary

print("\n--- Program 34: .clear() Method ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}
print("Original:", car)

car.clear()
print("After clear:", car)    # {}


print("\n" + "=" * 80)
print("SECTION 7: CHECKING FOR KEYS IN DICTIONARY")
print("=" * 80)

# program 35 - checking if key exists with 'in'
# returns True or False

print("\n--- Program 35: Checking Key with 'in' ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

print("Dictionary:", car)
print("'brand' in car:", "brand" in car)    # True
print("'color' in car:", "color" in car)    # False


# program 36 - using 'in' with if statement
# conditional check before accessing

print("\n--- Program 36: 'in' with if Statement ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

if "year" in car:
    print("Year:", car["year"])
else:
    print("Year not found")


# program 37 - checking if key NOT in dictionary
# using 'not in' operator

print("\n--- Program 37: Checking with 'not in' ---")

car = {"brand": "Toyota", "model": "Camry"}

if "color" not in car:
    print("Color is not in the dictionary")
    car["color"] = "blue"
    print("Added color:", car)


print("\n" + "=" * 80)
print("SECTION 8: LOOPING THROUGH DICTIONARIES")
print("=" * 80)

# program 38 - looping through keys
# default loop behavior

print("\n--- Program 38: Looping Through Keys ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

print("Keys:")
for key in car:
    print(key)


# program 39 - looping through keys explicitly
# using .keys() method

print("\n--- Program 39: Looping with .keys() ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

print("Keys:")
for key in car.keys():
    print(key)


# program 40 - looping through values
# using .values() method

print("\n--- Program 40: Looping Through Values ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

print("Values:")
for value in car.values():
    print(value)


# program 41 - looping through key-value pairs
# using .items() method

print("\n--- Program 41: Looping Through Items ---")

car = {"brand": "Toyota", "model": "Camry", "year": 2021}

print("Key-Value Pairs:")
for key, value in car.items():
    print(f"{key}: {value}")


# program 42 - looping through nested dictionary
# accessing nested values in loop

print("\n--- Program 42: Looping Through Nested Dictionary ---")

classroom = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print("Students:")
for student_id, details in classroom.items():
    print(f"{student_id}: {details['name']}, Age: {details['age']}")


print("\n" + "=" * 80)
print("SECTION 9: DICTIONARY COMPREHENSION")
print("=" * 80)

# program 43 - basic dictionary comprehension
# creating dictionary with comprehension

print("\n--- Program 43: Basic Dictionary Comprehension ---")

squares = {x: x**2 for x in range(1, 6)}
print("Squares:", squares)    # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# program 44 - dictionary comprehension with condition
# filtering values

print("\n--- Program 44: Comprehension with Condition ---")

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print("Even squares:", even_squares)    # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}


# program 45 - creating dictionary from two lists
# using zip() with comprehension

print("\n--- Program 45: Dictionary from Two Lists ---")

keys = ["name", "age", "city"]
values = ["John", 25, "New York"]

person = {k: v for k, v in zip(keys, values)}
print("Person:", person)    # {'name': 'John', 'age': 25, 'city': 'New York'}


print("\n" + "=" * 80)
print("SECTION 10: COPYING DICTIONARIES")
print("=" * 80)

# program 46 - copying with = (reference copy)
# both variables point to same dictionary

print("\n--- Program 46: Reference Copy (=) ---")

car1 = {"brand": "Toyota", "model": "Camry"}
car2 = car1

print("Original car1:", car1)
print("car2 (reference):", car2)

car2["year"] = 2021
print("\nAfter modifying car2:")
print("car1:", car1)    # also changed!
print("car2:", car2)


# program 47 - shallow copy with .copy()
# creates new dictionary with same items

print("\n--- Program 47: Shallow Copy (.copy()) ---")

car1 = {"brand": "Toyota", "model": "Camry"}
car2 = car1.copy()

print("Original car1:", car1)
print("car2 (copy):", car2)

car2["year"] = 2021
print("\nAfter modifying car2:")
print("car1:", car1)    # not changed
print("car2:", car2)


# program 48 - shallow copy with dict()
# another way to copy

print("\n--- Program 48: Copy with dict() ---")

car1 = {"brand": "Toyota", "model": "Camry"}
car2 = dict(car1)

print("Original car1:", car1)
print("car2 (copy):", car2)

car2["year"] = 2021
print("\nAfter modifying car2:")
print("car1:", car1)    # not changed
print("car2:", car2)


print("\n" + "=" * 80)
print("SECTION 11: MERGING DICTIONARIES")
print("=" * 80)

# program 49 - merging with .update()
# modifies first dictionary

print("\n--- Program 49: Merging with .update() ---")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

print("dict1:", dict1)
print("dict2:", dict2)

dict1.update(dict2)
print("After merge:", dict1)    # {'a': 1, 'b': 3, 'c': 4}


# program 50 - merging with unpacking operator **
# creates new dictionary

print("\n--- Program 50: Merging with ** Operator ---")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

print("dict1:", dict1)
print("dict2:", dict2)

merged = {**dict1, **dict2}
print("Merged:", merged)    # {'a': 1, 'b': 3, 'c': 4}
print("dict1 unchanged:", dict1)
print("dict2 unchanged:", dict2)


# program 51 - merging with | operator (Python 3.9+)
# union operator for dictionaries

print("\n--- Program 51: Merging with | Operator ---")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

print("dict1:", dict1)
print("dict2:", dict2)

merged = dict1 | dict2
print("Merged:", merged)    # {'a': 1, 'b': 3, 'c': 4}


print("\n" + "=" * 80)
print("SECTION 12: PRACTICAL DICTIONARY OPERATIONS")
print("=" * 80)

# program 52 - counting occurrences
# using dictionary to count items

print("\n--- Program 52: Counting Occurrences ---")

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = {}
for fruit in fruits:
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

print("Fruits:", fruits)
print("Count:", count)    # {'apple': 3, 'banana': 2, 'orange': 1}


# program 53 - grouping data
# organizing items by category

print("\n--- Program 53: Grouping Data ---")

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]

by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

print("Students:", students)
print("Grouped by grade:", by_grade)


# program 54 - inverting dictionary
# swapping keys and values

print("\n--- Program 54: Inverting Dictionary ---")

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

print("Original:", original)
print("Inverted:", inverted)    # {1: 'a', 2: 'b', 3: 'c'}


# program 55 - filtering dictionary
# removing items based on condition

print("\n--- Program 55: Filtering Dictionary ---")

scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "Diana": 68}

passed = {name: score for name, score in scores.items() if score >= 75}

print("All scores:", scores)
print("Passed (>=75):", passed)    # {'Alice': 85, 'Charlie': 90}


print("\n" + "=" * 80)
print("END OF DICTIONARY CONCEPT PRACTICE")
print("=" * 80)
