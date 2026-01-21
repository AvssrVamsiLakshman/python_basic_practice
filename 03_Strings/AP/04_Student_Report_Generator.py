# ============================================================
# AP 04: Student Report Generator
# ============================================================
# Description: Accept student name, subject, and score.
#              Clean inputs, format output using .format() and f-strings.
# ============================================================

# Prompt user to enter student information
student_name = input("Enter student name: ")
subject = input("Enter subject: ")
score = input("Enter score: ")

# Clean each input using strip()
student_name = student_name.strip()
subject = subject.strip()
score = score.strip()

# Convert name to lowercase and subject to title case
name_lower = student_name.lower()
subject_title = subject.title()

# Create a divider line using repetition
divider = "*" * 40

# Construct sentences using .format() and f-string
format_sentence = "Student {} has scored {} in {}.".format(student_name.title(), score, subject_title)
fstring_sentence = f"{name_lower}'s performance in {subject_title} is satisfactory."

# Display output
print()
print(divider)
print(format_sentence)
print(fstring_sentence)
print(divider)
