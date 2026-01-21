# ============================================================
# Concept: String Formatting
# Topic: Nested Formatting
# ============================================================
# Description: Combining positional arguments with nested
#              formatting and format specifiers.
# ============================================================

# Combining positional arguments with nested formatting.
text = "The price of {0} is {1:.2f}. With tax, it becomes {2:.2f}.".format("a book", 12.49, 12.49 * 1.07)

print(text)
# Output: The price of a book is 12.49. With tax, it becomes 13.36.
