"""
# Description of the Task
Create a Python program that takes a student's marks as input and prints the corresponding grade based on predefined criteria.

# Instructions
Prompt the user to enter the student's marks (a number between 0 and 100).
Use if-else statements to determine the grade based on the following criteria:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: below 60
Print the corresponding grade.

# Learning Objective
To practice using if-else statements.
To understand how to implement conditional logic in a Python program.
To gain experience with basic input and output operations in Python.

# Sample Usage
Enter the student's marks: 85
Grade: B
Enter the student's marks: 72
Grade: C
Enter the student's marks: 59
Grade: F
"""

print("=" * 80)
print("GRADE CALCULATOR PROGRAM")
print("=" * 80)

# Step 1: Prompt user to enter marks
print("\nGrading Criteria:")
print("  A: 90-100")
print("  B: 80-89")
print("  C: 70-79")
print("  D: 60-69")
print("  F: below 60")

print("\n" + "-" * 80)
marks_input = input("Enter the student's marks (0-100): ")

# Convert to number and validate
try:
    marks = float(marks_input)
    
    # Step 2: Validate marks range
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100")
    else:
        # Step 3: Determine grade using if-elif-else
        print("-" * 80)
        
        if marks >= 90:
            grade = "A"
            performance = "Excellent"
        elif marks >= 80:
            grade = "B"
            performance = "Very Good"
        elif marks >= 70:
            grade = "C"
            performance = "Good"
        elif marks >= 60:
            grade = "D"
            performance = "Satisfactory"
        else:
            grade = "F"
            performance = "Fail"
        
        # Display result
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")
        print(f"Performance: {performance}")
        
except ValueError:
    print("Error: Please enter a valid number")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test with multiple marks
test_marks = [95, 85, 72, 65, 59, 45, 100, 0]

print("\nGrade calculation for sample marks:")
for mark in test_marks:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"  Marks: {mark:3} → Grade: {grade}")


# Enhanced grading with plus/minus
print("\n" + "=" * 80)
print("BONUS: Enhanced Grading with Plus/Minus")
print("=" * 80)

def get_detailed_grade(marks):
    """Get grade with plus/minus modifiers"""
    if marks >= 97:
        return "A+"
    elif marks >= 93:
        return "A"
    elif marks >= 90:
        return "A-"
    elif marks >= 87:
        return "B+"
    elif marks >= 83:
        return "B"
    elif marks >= 80:
        return "B-"
    elif marks >= 77:
        return "C+"
    elif marks >= 73:
        return "C"
    elif marks >= 70:
        return "C-"
    elif marks >= 67:
        return "D+"
    elif marks >= 63:
        return "D"
    elif marks >= 60:
        return "D-"
    else:
        return "F"

# Test enhanced grading
print("\nEnhanced grading examples:")
sample_scores = [98, 91, 85, 77, 65, 55]

for score in sample_scores:
    detailed_grade = get_detailed_grade(score)
    print(f"  Marks: {score} → Grade: {detailed_grade}")


# GPA calculation
print("\n" + "=" * 80)
print("BONUS: GPA Calculation")
print("=" * 80)

def calculate_gpa(marks):
    """Calculate GPA based on marks"""
    if marks >= 90:
        return 4.0
    elif marks >= 80:
        return 3.0
    elif marks >= 70:
        return 2.0
    elif marks >= 60:
        return 1.0
    else:
        return 0.0

print("\nGPA calculation examples:")
for mark in [95, 85, 75, 65, 55]:
    gpa = calculate_gpa(mark)
    grade = "A" if mark >= 90 else "B" if mark >= 80 else "C" if mark >= 70 else "D" if mark >= 60 else "F"
    print(f"  Marks: {mark} → Grade: {grade} → GPA: {gpa}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
