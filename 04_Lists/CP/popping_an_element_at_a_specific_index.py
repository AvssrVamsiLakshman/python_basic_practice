# ============================================================
# Concept: List Methods - pop()
# Topic: Popping an Element at a Specific Index
# ============================================================
# Description: Using pop() with an index to remove and return
#              an element at that specific position.
# ============================================================

numbers = [10, 20, 30, 40]

second_number = numbers.pop(1)

print("Removed number:", second_number)
# Output: Removed number: 20

print("Updated list:", numbers)
# Output: Updated list: [10, 30, 40]
