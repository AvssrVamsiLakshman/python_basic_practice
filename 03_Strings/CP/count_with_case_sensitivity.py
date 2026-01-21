# ============================================================
# Concept: String Methods - count()
# Topic: Count with Case Sensitivity
# ============================================================
# Description: count() is case-sensitive. 'Hello' and 'hello'
#              are counted separately.
# ============================================================

text = "Hello hello"
count = text.count("hello")

print(count)
# Output: 1
