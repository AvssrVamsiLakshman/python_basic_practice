print("=" * 80)
print("SECTION 1: CREATING AND ACCESSING LISTS")
print("=" * 80)

# program 1 - basic list
# making a list with square brackets []

print("\n--- Program 1: Creating Basic List ---")

fruits = ["apple", "banana", "orange"]

print("List:", fruits)


# program 2 - indexing (positive)
# accessing items using position (starts from 0!)

print("\n--- Program 2: Positive Indexing ---")

fruits = ["apple", "banana", "orange"]

print("List:", fruits)
print("First item (index 0):", fruits[0])      # apple
print("Second item (index 1):", fruits[1])     # banana
print("Third item (index 2):", fruits[2])      # orange


# program 3 - indexing (negative)
# counting from end using negative numbers
# -1 is last item!

print("\n--- Program 3: Negative Indexing ---")

fruits = ["apple", "banana", "orange"]

print("List:", fruits)
print("Last item (-1):", fruits[-1])      # orange
print("Second last (-2):", fruits[-2])    # banana
print("First item (-3):", fruits[-3])     # apple


# program 4 - slicing
# getting multiple items using start:end
# important: end index not included!

print("\n--- Program 4: Slicing ---")

numbers = [1, 2, 3, 4, 5]

print("List:", numbers)
print("First 3 items [0:3]:", numbers[0:3])    # [1, 2, 3]
print("From index 2 [2:]:", numbers[2:])       # [3, 4, 5]
print("Up to index 3 [:3]:", numbers[:3])      # [1, 2, 3]


print("\n" + "=" * 80)
print("SECTION 2: ADDING ITEMS TO LIST")
print("=" * 80)

# program 5 - append()
# adds item to end of list
# most common way to add items!

print("\n--- Program 5: append() Method ---")

fruits = ["apple", "banana"]
print("Original:", fruits)

fruits.append("orange")
print("After append:", fruits)    # ['apple', 'banana', 'orange']


# program 6 - append() multiple times
# can keep appending

print("\n--- Program 6: Multiple appends ---")

fruits = ["apple"]
print("Start:", fruits)

fruits.append("banana")
fruits.append("orange")
fruits.append("mango")
print("After multiple appends:", fruits)


# program 7 - insert()
# adds item at specific position
# syntax: list.insert(position, item)

print("\n--- Program 7: insert() Method ---")

fruits = ["apple", "orange"]
print("Original:", fruits)

fruits.insert(1, "banana")    # insert at index 1
print("After insert:", fruits)    # ['apple', 'banana', 'orange']


# program 8 - insert() at beginning
# inserting at index 0

print("\n--- Program 8: insert() at Start ---")

numbers = [2, 3, 4]
print("Original:", numbers)

numbers.insert(0, 1)    # insert at beginning
print("After insert:", numbers)    # [1, 2, 3, 4]


# program 9 - extend()
# adds multiple items from another list
# different from append!

print("\n--- Program 9: extend() Method ---")

fruits = ["apple", "banana"]
more_fruits = ["orange", "mango"]

print("List 1:", fruits)
print("List 2:", more_fruits)

fruits.extend(more_fruits)
print("After extend:", fruits)    # ['apple', 'banana', 'orange', 'mango']


# program 10 - extend() vs append()
# showing the difference
# append adds whole list as one item, extend adds each item separately

print("\n--- Program 10: extend() vs append() ---")

# using extend
list1 = ["a", "b"]
list1.extend(["c", "d"])
print("With extend:", list1)    # ['a', 'b', 'c', 'd']

# using append
list2 = ["a", "b"]
list2.append(["c", "d"])
print("With append:", list2)    # ['a', 'b', ['c', 'd']] - nested!


print("\n" + "=" * 80)
print("SECTION 3: REMOVING ITEMS FROM LIST")
print("=" * 80)

# program 11 - remove()
# removes first occurrence of value
# gives error if value not in list!

print("\n--- Program 11: remove() Method ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)    # ['apple', 'orange']


# program 12 - remove() first occurrence
# only removes first match

print("\n--- Program 12: remove() First Match ---")

numbers = [1, 2, 3, 2, 4]
print("Original:", numbers)

numbers.remove(2)    # removes first 2
print("After remove:", numbers)    # [1, 3, 2, 4]


# program 13 - pop()
# removes and returns last item

print("\n--- Program 13: pop() Method ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

removed = fruits.pop()
print("Removed item:", removed)         # orange
print("List after pop:", fruits)        # ['apple', 'banana']


# program 14 - pop() with index
# can remove item at specific position

print("\n--- Program 14: pop() with Index ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

removed = fruits.pop(1)    # remove index 1
print("Removed item:", removed)      # banana
print("List after pop:", fruits)     # ['apple', 'orange']


# program 15 - del keyword
# deletes item at index
# or can delete entire list!

print("\n--- Program 15: del Keyword ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

del fruits[1]    # delete index 1
print("After del:", fruits)    # ['apple', 'orange']


# program 16 - del with slicing
# can delete multiple items

print("\n--- Program 16: del with Slice ---")

numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)

del numbers[1:3]    # delete index 1 and 2
print("After del:", numbers)    # [1, 4, 5]


# program 17 - clear()
# removes all items, leaves empty list

print("\n--- Program 17: clear() Method ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

fruits.clear()
print("After clear:", fruits)    # []


print("\n" + "=" * 80)
print("SECTION 4: FINDING ITEMS IN LIST")
print("=" * 80)

# program 18 - index()
# finds position of item
# gives error if not found!

print("\n--- Program 18: index() Method ---")

fruits = ["apple", "banana", "orange"]

position = fruits.index("banana")
print("List:", fruits)
print("Position of 'banana':", position)    # 1


# program 19 - index() with start and end
# can search in specific range

print("\n--- Program 19: index() with Range ---")

numbers = [1, 2, 3, 2, 4]

position = numbers.index(2, 2)    # find 2 starting from index 2
print("List:", numbers)
print("Position of 2 (from index 2):", position)    # 3


# program 20 - count()
# counts how many times item appears

print("\n--- Program 20: count() Method ---")

numbers = [1, 2, 2, 3, 2, 4]

count = numbers.count(2)
print("List:", numbers)
print("Count of 2:", count)    # 3


# program 21 - in operator
# checks if item exists in list
# returns True or False

print("\n--- Program 21: 'in' Operator ---")

fruits = ["apple", "banana", "orange"]

print("List:", fruits)
print("'banana' in list:", "banana" in fruits)      # True
print("'mango' in list:", "mango" in fruits)        # False


print("\n" + "=" * 80)
print("SECTION 5: SORTING AND REVERSING")
print("=" * 80)

# program 22 - sort()
# sorts list in ascending order
# changes original list!

print("\n--- Program 22: sort() Method ---")

numbers = [3, 1, 4, 1, 5]
print("Original:", numbers)

numbers.sort()
print("After sort:", numbers)    # [1, 1, 3, 4, 5]


# program 23 - sort() descending
# sort in reverse order

print("\n--- Program 23: sort() Descending ---")

numbers = [3, 1, 4, 1, 5]
print("Original:", numbers)

numbers.sort(reverse=True)
print("After sort:", numbers)    # [5, 4, 3, 1, 1]


# program 24 - reverse()
# reverses order of list
# not same as sort!

print("\n--- Program 24: reverse() Method ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

fruits.reverse()
print("After reverse:", fruits)    # ['orange', 'banana', 'apple']


print("\n" + "=" * 80)
print("SECTION 6: LIST OPERATIONS")
print("=" * 80)

# program 25 - concatenation (+)
# joining two lists together

print("\n--- Program 25: List Concatenation ---")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print("List 1:", list1)
print("List 2:", list2)
print("Combined:", combined)    # [1, 2, 3, 4, 5, 6]


# program 26 - repetition (*)
# repeating list multiple times

print("\n--- Program 26: List Repetition ---")

numbers = [1, 2]
repeated = numbers * 3

print("Original:", numbers)
print("Repeated 3 times:", repeated)    # [1, 2, 1, 2, 1, 2]


# program 27 - len()
# gets number of items in list

print("\n--- Program 27: List Length ---")

fruits = ["apple", "banana", "orange"]

length = len(fruits)
print("List:", fruits)
print("Length:", length)    # 3


# program 28 - min() and max()
# finds smallest and largest items

print("\n--- Program 28: min() and max() ---")

numbers = [3, 1, 4, 1, 5, 9, 2]

print("List:", numbers)
print("Minimum:", min(numbers))    # 1
print("Maximum:", max(numbers))    # 9


# program 29 - sum()
# adds all numbers in list

print("\n--- Program 29: sum() Function ---")

numbers = [1, 2, 3, 4, 5]

total = sum(numbers)
print("List:", numbers)
print("Sum:", total)    # 15


print("\n" + "=" * 80)
print("SECTION 7: COPYING LISTS")
print("=" * 80)

# program 30 - copy()
# makes a copy of list

print("\n--- Program 30: copy() Method ---")

original = [1, 2, 3]
copied = original.copy()

print("Original:", original)
print("Copied:", copied)

# modifying copy doesn't affect original
copied.append(4)
print("\nAfter modifying copy:")
print("Original:", original)    # [1, 2, 3] - unchanged!
print("Copied:", copied)        # [1, 2, 3, 4]


# program 31 - copy using slicing
# another way to copy

print("\n--- Program 31: Copy using Slice [:] ---")

original = [1, 2, 3]
copied = original[:]

copied.append(4)
print("Original:", original)    # [1, 2, 3]
print("Copied:", copied)        # [1, 2, 3, 4]


print("\n" + "=" * 80)
print("SECTION 8: NESTED LISTS")
print("=" * 80)

# program 32 - nested list basic
# list inside list!

print("\n--- Program 32: Nested List ---")

nested = [[1, 2], [3, 4], [5, 6]]

print("Nested list:", nested)
print("First inner list:", nested[0])      # [1, 2]
print("Second inner list:", nested[1])     # [3, 4]


# program 33 - accessing nested items
# need two indices: [outer][inner]

print("\n--- Program 33: Accessing Nested Items ---")

nested = [[1, 2], [3, 4], [5, 6]]

print("Nested list:", nested)
print("Item [0][0]:", nested[0][0])    # 1
print("Item [1][1]:", nested[1][1])    # 4
print("Item [2][0]:", nested[2][0])    # 5


# program 34 - 2D list (matrix)
# like a table with rows and columns

print("\n--- Program 34: 2D List (Matrix) ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)


# program 35 - accessing matrix elements
# [row][column]

print("\n--- Program 35: Matrix Element Access ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element at row 0, col 0:", matrix[0][0])    # 1
print("Element at row 1, col 2:", matrix[1][2])    # 6
print("Element at row 2, col 1:", matrix[2][1])    # 8


print("\n" + "=" * 80)
print("SECTION 9: MODIFYING LISTS")
print("=" * 80)

# program 36 - changing item
# can change item by assigning to index

print("\n--- Program 36: Modifying Single Item ---")

fruits = ["apple", "banana", "orange"]
print("Original:", fruits)

fruits[1] = "mango"    # change index 1
print("After change:", fruits)    # ['apple', 'mango', 'orange']


# program 37 - changing multiple items
# using slicing

print("\n--- Program 37: Modifying Multiple Items ---")

numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)

numbers[1:3] = [20, 30]    # change indices 1 and 2
print("After change:", numbers)    # [1, 20, 30, 4, 5]


# program 38 - modifying nested list
# changing items in nested list

print("\n--- Program 38: Modifying Nested List ---")

nested = [[1, 2], [3, 4]]
print("Original:", nested)

nested[0][1] = 20    # change [0][1] to 20
print("After change:", nested)    # [[1, 20], [3, 4]]


print("\n" + "=" * 80)
print("SECTION 10: LIST COMPREHENSION")
print("=" * 80)

# program 39 - basic list comprehension
# shortcut to create lists

print("\n--- Program 39: List Comprehension ---")

# normal way
squares1 = []
for i in range(5):
    squares1.append(i ** 2)

# list comprehension way
squares2 = [i ** 2 for i in range(5)]

print("Normal way:", squares1)            # [0, 1, 4, 9, 16]
print("List comprehension:", squares2)    # [0, 1, 4, 9, 16]


# program 40 - list comprehension with condition
# can add if to filter

print("\n--- Program 40: Comprehension with Filter ---")

# only even numbers
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]

print("Original:", numbers)
print("Even numbers:", evens)    # [2, 4, 6]


print("\n" + "=" * 80)
print("DONE! ALL 40 LIST PROGRAMS COMPLETED")
print("=" * 80)
