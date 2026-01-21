# ============================================================
# Concept: String Methods - endswith()
# Topic: using len() function within
# ============================================================
# Description: Using len() function within endswith() to
#              dynamically set the end argument.
# ============================================================

text = "Python programming is powerful"

print(text.endswith("powerful", 0, len(text)))
#Output: True
