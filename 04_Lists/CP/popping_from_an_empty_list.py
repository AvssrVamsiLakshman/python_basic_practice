# ============================================================
# Concept: List Methods - pop()
# Topic: Popping from an Empty List
# ============================================================
# Description: Attempting to pop from an empty list raises
#              an IndexError.
# ============================================================

empty_list = []

popped_item = empty_list.pop()

print("Popped item:", popped_item)

# Output:
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 5, in <module>
# IndexError: pop from empty list
