# ============================================================
# Concept: String Formatting
# Topic: Reusing Positional Arguments
# ============================================================
# Description: Reusing positional arguments multiple times
#              in the format string.
# ============================================================

# Reusing positional arguments multiple times.
text = "{0} loves {1}. {0} enjoys {1} a lot.".format("Bob", "reading")

print(text)
# Output: Bob loves reading. Bob enjoys reading a lot.
