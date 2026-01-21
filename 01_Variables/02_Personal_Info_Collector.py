# promt "First Name, Last Name, Age, City"

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city of residence: ")

# combine first and last name and print full name age city

full_name = first_name + " " + last_name
print("Full Name:", full_name)
print("City:", city)
print("Age:", age)

# print data types of each variable
print("\nData Types:")
print("full_name:", type(full_name))
print("age:", type(age))
print("city:", type(city))

# calculate length of full name and print character count
length_of_full_name = len(full_name)
print("\nLength of full name:", length_of_full_name, "characters")

# convert age to number, add 5 and print future age
future_age = int(age) + 5
print("\nIn 5 years, you will be", future_age, "years old.")
