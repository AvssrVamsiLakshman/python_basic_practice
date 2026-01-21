# ============================================================
# Concept: String Formatting
# Topic: Nested Formatting (Keyword)
# ============================================================
# Description: Combining keyword arguments with nested
#              formatting and format specifiers.
# ============================================================

# Combining keyword arguments with nested formatting.
text = "The price of {item} is ${price:.2f}. With tax, it becomes ${total:.2f}.".format(item="a book", price=12.49, total=12.49 * 1.07)

print(text)
# Output: The price of a book is $12.49. With tax, it becomes $13.36.
