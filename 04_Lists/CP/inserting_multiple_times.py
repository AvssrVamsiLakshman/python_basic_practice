# ============================================================
# Concept: List Methods - insert()
# Topic: Inserting Multiple Times
# ============================================================
# Description: Using insert() multiple times to add elements
#              at different positions.
# ============================================================

movies = ["Inception", "Avatar"]

movies.insert(1, "Titanic")

movies.insert(0, "The Matrix")

print(movies)

# Output: ['The Matrix', 'Inception', 'Titanic', 'Avatar']
