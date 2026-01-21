# ============================================================
# Concept: String Methods - split()
# Topic: Handling Multiple Consecutive Delimiters
# ============================================================
# Description: When there are consecutive delimiters, split()
#              creates empty strings in the result.
# ============================================================

text = "a,,b,,c"
split_text = text.split(",")

print(split_text)
# Output: ['a', '', 'b', '', 'c']
