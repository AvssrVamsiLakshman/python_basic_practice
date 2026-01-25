"""
# Description of the Task: 
Create a Python program that demonstrates the use of dictionaries. Dictionaries are a fundamental data structure in Python used to store key-value pairs.

# Instructions:
Create a dictionary to store information about a person. Include keys such as "name", "age", "city", "country", etc.
Print the dictionary.
Update the dictionary to include additional information.
Print the updated dictionary.
Access and print specific values from the dictionary using their keys.

# Learning Objective:
Understanding dictionaries and their syntax in Python.
Practicing dictionary manipulation including adding, updating, and accessing key-value pairs.
"""

# Step 1: Create a dictionary to store information about a person
print("=" * 80)
print("STEP 1: Creating a Person Dictionary")
print("=" * 80)

person = {
    "name": "Alex Johnson",
    "age": 28,
    "city": "San Francisco",
    "country": "USA"
}

# Step 2: Print the dictionary
print("\nOriginal Person Dictionary:")
print(person)


# Step 3: Update the dictionary to include additional information
print("\n" + "=" * 80)
print("STEP 2: Updating the Dictionary")
print("=" * 80)

# Adding new key-value pairs
person["occupation"] = "Software Engineer"
person["email"] = "alex.johnson@email.com"
person["phone"] = "+1-555-0123"

# Updating existing value
person["age"] = 29  # birthday!

print("\nUpdated Person Dictionary:")
print(person)


# Step 4: Access and print specific values from the dictionary using their keys
print("\n" + "=" * 80)
print("STEP 3: Accessing Specific Values")
print("=" * 80)

print(f"\nName: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
print(f"Country: {person['country']}")
print(f"Occupation: {person['occupation']}")
print(f"Email: {person['email']}")
print(f"Phone: {person['phone']}")


# Additional demonstrations
print("\n" + "=" * 80)
print("BONUS: Additional Dictionary Operations")
print("=" * 80)

# Using .get() method for safe access
print("\nUsing .get() method:")
hobby = person.get("hobby", "Not specified")
print(f"Hobby: {hobby}")

# Checking if a key exists
print("\nChecking if keys exist:")
print(f"'email' in person: {'email' in person}")
print(f"'salary' in person: {'salary' in person}")

# Getting all keys and values
print("\nAll keys:", list(person.keys()))
print("All values:", list(person.values()))

print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
