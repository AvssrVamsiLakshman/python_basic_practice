# ============================================================
# Concept: String Formatting
# Topic: Reusing Keyword Arguments
# ============================================================
# Description: Reusing the same keyword argument multiple
#              times in the string.
# ============================================================

# Reusing the same keyword argument multiple times in the string.
text = "{name} loves {hobby}. {name} also enjoys {hobby} on weekends.".format(name="Bob", hobby="cycling")

print(text)
# Output: Bob loves cycling. Bob also enjoys cycling on weekends.
