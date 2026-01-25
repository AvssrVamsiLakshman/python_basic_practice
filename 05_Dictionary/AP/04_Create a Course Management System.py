"""
Task Objective:
• Create a nested dictionary named course_data to manage university course enrollments.
• Store structured details like instructor, credits, and enrolled_students.
• Modify the student list and course details.
• Add a new course with complete data.
• Access data from a course that may not exist using the get() method.

📝 Instructions:
• Define a dictionary named course_data with at least two courses: CS101 and MATH123.
  - Each should store:
    • instructor (string)
    • credits (int)
    • enrolled_students (list of strings)
• Add a new student to the enrolled_students list for CS101.
• Update the number of credits for MATH123.
• Add a new course PHY202 with full details.
• Print the entire updated dictionary.
• Use the get() method to check if a course BIO150 exists and return "Course not available" if not.

💡 Sample Output:

Updated CS101: ['Alice', 'Bob', 'Charlie']  
Updated MATH123 credits: 4  
Added course PHY202: {'instructor': 'Dr. Lee', 'credits': 3, 'enrolled_students': ['Sam', 'Nina']}

Full Course Data:  
{'CS101': {'instructor': 'Dr. Smith', 'credits': 3, 'enrolled_students': ['Alice', 'Bob', 'Charlie']},  
 'MATH123': {'instructor': 'Dr. Brown', 'credits': 4, 'enrolled_students': ['Tom']},  
 'PHY202': {'instructor': 'Dr. Lee', 'credits': 3, 'enrolled_students': ['Sam', 'Nina']}}

BIO150: Course not available
"""

print("=" * 80)
print("COURSE MANAGEMENT SYSTEM")
print("=" * 80)

# Step 1: Define course_data dictionary with CS101 and MATH123
print("\nSTEP 1: Creating Course Data with Initial Courses")
print("-" * 80)

course_data = {
    "CS101": {
        "instructor": "Dr. Smith",
        "credits": 3,
        "enrolled_students": ["Alice", "Bob"]
    },
    "MATH123": {
        "instructor": "Dr. Brown",
        "credits": 3,  # Will be updated to 4
        "enrolled_students": ["Tom"]
    }
}

print("Initial Course Data:")
for course_code, details in course_data.items():
    print(f"\n  {course_code}:")
    print(f"    Instructor: {details['instructor']}")
    print(f"    Credits: {details['credits']}")
    print(f"    Enrolled Students: {details['enrolled_students']}")


# Step 2: Add a new student to CS101's enrolled_students list
print("\n" + "=" * 80)
print("STEP 2: Adding New Student to CS101")
print("-" * 80)

course_data["CS101"]["enrolled_students"].append("Charlie")
print(f"Updated CS101 students: {course_data['CS101']['enrolled_students']}")


# Step 3: Update the number of credits for MATH123
print("\n" + "=" * 80)
print("STEP 3: Updating Credits for MATH123")
print("-" * 80)

course_data["MATH123"]["credits"] = 4
print(f"Updated MATH123 credits: {course_data['MATH123']['credits']}")


# Step 4: Add a new course PHY202 with full details
print("\n" + "=" * 80)
print("STEP 4: Adding New Course PHY202")
print("-" * 80)

course_data["PHY202"] = {
    "instructor": "Dr. Lee",
    "credits": 3,
    "enrolled_students": ["Sam", "Nina"]
}

print(f"Added course PHY202: {course_data['PHY202']}")


# Step 5: Print the entire updated dictionary
print("\n" + "=" * 80)
print("STEP 5: Full Course Data")
print("-" * 80)

print("\nFull Course Data:")
for course_code, details in course_data.items():
    print(f"\n{course_code}:")
    print(f"  Instructor: {details['instructor']}")
    print(f"  Credits: {details['credits']}")
    print(f"  Enrolled Students: {details['enrolled_students']}")


# Step 6: Use get() method to check if BIO150 exists
print("\n" + "=" * 80)
print("STEP 6: Safe Access Using .get() Method")
print("-" * 80)

# Checking for non-existent course
bio150_info = course_data.get("BIO150", "Course not available")
print(f"\nBIO150: {bio150_info}")


# Additional demonstrations
print("\n" + "=" * 80)
print("BONUS: Additional Course Statistics")
print("-" * 80)

# Total number of courses
print(f"\nTotal Courses: {len(course_data)}")

# Total enrolled students across all courses
total_students = sum(len(details['enrolled_students']) 
                    for details in course_data.values())
print(f"Total Enrolled Students: {total_students}")

# List all instructors
print("\nAll Instructors:")
instructors = [details['instructor'] for details in course_data.values()]
for instructor in instructors:
    print(f"  • {instructor}")

# Total credits offered
total_credits = sum(details['credits'] for details in course_data.values())
print(f"\nTotal Credits Offered: {total_credits}")

# Find courses with more than 1 student
print("\nCourses with Multiple Students:")
for course_code, details in course_data.items():
    if len(details['enrolled_students']) > 1:
        print(f"  {course_code}: {len(details['enrolled_students'])} students")

# Find student enrollment
print("\nStudent Enrollment Details:")
all_students = {}
for course_code, details in course_data.items():
    for student in details['enrolled_students']:
        if student not in all_students:
            all_students[student] = []
        all_students[student].append(course_code)

for student, courses in all_students.items():
    print(f"  {student}: {', '.join(courses)}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
