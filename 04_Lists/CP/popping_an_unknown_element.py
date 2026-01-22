# ============================================================
# Concept: List Methods - pop()
# Topic: Popping an Unknown Element
# ============================================================
# Description: Attempting to pop at an index that doesn't
#              exist raises an IndexError.
# ============================================================

colors = ["red", "green", "blue"]

index_to_pop = 5
popped_color = colors.pop(index_to_pop)

print("Popped color:", popped_color)

# output :
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 8, in <module>
# IndexError: pop index out of range
