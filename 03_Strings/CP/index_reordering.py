# ============================================================
# Concept: String Formatting
# Topic: Index Reordering
# ============================================================
# Description: Reordering positional arguments in the format
#              string by specifying index.
# ============================================================

# Reordering positional arguments in the format string.
text = "{1} is the name of the person. {0} is their age.".format(25, "David")

print(text)
# Output: David is the name of the person. 25 is their age.
