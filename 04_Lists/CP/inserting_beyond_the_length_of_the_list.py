# ============================================================
# Concept: List Methods - insert()
# Topic: Inserting Beyond the Length of the List
# ============================================================
# Description: When inserting at an index beyond the list
#              length, the element is added at the end.
# ============================================================

animals = ["dog", "cat"]

animals.insert(5, "fish")

print(animals)  # Output: ['dog', 'cat', 'fish']
