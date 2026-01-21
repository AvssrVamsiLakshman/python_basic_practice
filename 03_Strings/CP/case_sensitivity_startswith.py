# ============================================================
# Concept: String Methods - startswith()
# Topic: Case Sensitivity
# ============================================================
# Description: startswith() is case-sensitive. 'Hello' and
#              'hello' are different.
# ============================================================

text = "Hello World"
starts = text.startswith("hello")

print(starts)
# Output: False
