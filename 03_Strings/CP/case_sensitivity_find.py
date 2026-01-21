# ============================================================
# Concept: String Methods - find()
# Topic: Case Sensitivity
# ============================================================
# Description: find() is case-sensitive. 'World' and 'world'
#              are treated as different substrings.
# ============================================================

text = "Hello World"
index = text.find("world")

print(index)
# Output: -1
