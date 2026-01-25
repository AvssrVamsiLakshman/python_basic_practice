"""
# Description of the Task
Create a Python program that takes a password as input from the user and checks if it meets the following criteria:
At least 8 characters long
Contains both uppercase and lowercase letters
Contains at least one numeric digit

# Instructions
Prompt the user to enter a password.
Check if the password is at least 8 characters long.
Check if the password contains both uppercase and lowercase letters.
Check if the password contains at least one numeric digit.
Inform the user whether the password meets all the criteria or not.

# Learning Objective
This task helps beginners practice using:
Input and output functions
Conditional statements (if-else)
Loop structures (if needed)
String methods for checking character properties

# Sample Usage
Example Input:
Enter your password: Secure123
Example Output:
Password is valid.

Example Input:
Enter your password: short1
Example Output:
Password is invalid.
"""

print("=" * 80)
print("PASSWORD CHECKER PROGRAM")
print("=" * 80)

# Display password requirements
print("\nPassword Requirements:")
print("  • At least 8 characters long")
print("  • Contains both uppercase and lowercase letters")
print("  • Contains at least one numeric digit")

# Step 1: Prompt user to enter password
print("\n" + "-" * 80)
password = input("Enter your password: ")
print("-" * 80)

# Step 2: Check all criteria
# Initialize validation flags
is_length_valid = len(password) >= 8
has_uppercase = False
has_lowercase = False
has_digit = False

# Check each character
for char in password:
    if char.isupper():
        has_uppercase = True
    if char.islower():
        has_lowercase = True
    if char.isdigit():
        has_digit = True

# Step 3: Display detailed results
print("\nPassword Analysis:")
print(f"  Length (>= 8 characters): {'✓' if is_length_valid else '✗'} ({len(password)} characters)")
print(f"  Has uppercase letter: {'✓' if has_uppercase else '✗'}")
print(f"  Has lowercase letter: {'✓' if has_lowercase else '✗'}")
print(f"  Has digit: {'✓' if has_digit else '✗'}")

# Step 4: Final validation
print("\n" + "-" * 80)

if is_length_valid and has_uppercase and has_lowercase and has_digit:
    print("✓ Password is valid.")
else:
    print("✗ Password is invalid.")
    print("\nMissing requirements:")
    if not is_length_valid:
        print(f"  • Password must be at least 8 characters (current: {len(password)})")
    if not has_uppercase:
        print("  • Password must contain at least one uppercase letter")
    if not has_lowercase:
        print("  • Password must contain at least one lowercase letter")
    if not has_digit:
        print("  • Password must contain at least one digit")


# Additional demonstrations
print("\n" + "=" * 80)
print("ADDITIONAL EXAMPLES")
print("=" * 80)

# Test passwords
test_passwords = [
    "Secure123",
    "short1",
    "NoDigitsHere",
    "12345678",
    "alllowercase123",
    "ALLUPPERCASE123",
    "Valid1Pass",
    "weak"
]

print("\nTesting multiple passwords:")

for pwd in test_passwords:
    # Check criteria
    length_ok = len(pwd) >= 8
    upper_ok = any(c.isupper() for c in pwd)
    lower_ok = any(c.islower() for c in pwd)
    digit_ok = any(c.isdigit() for c in pwd)
    
    valid = length_ok and upper_ok and lower_ok and digit_ok
    
    status = "VALID" if valid else "INVALID"
    print(f"  {pwd:20} → {status}")


# Enhanced password checker
print("\n" + "=" * 80)
print("BONUS: Enhanced Password Checker with Special Characters")
print("=" * 80)

def check_password_strength(pwd):
    """
    Check password strength with additional criteria
    Returns: (is_valid, strength_level, missing_requirements)
    """
    # Basic requirements
    length_ok = len(pwd) >= 8
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    
    # Additional checks
    has_special = any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pwd)
    is_long = len(pwd) >= 12
    
    # Determine validity
    is_valid = length_ok and has_upper and has_lower and has_digit
    
    # Calculate strength
    strength_score = sum([length_ok, has_upper, has_lower, has_digit, has_special, is_long])
    
    if strength_score >= 5:
        strength = "Strong"
    elif strength_score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"
    
    # Missing requirements
    missing = []
    if not length_ok:
        missing.append("Minimum 8 characters")
    if not has_upper:
        missing.append("Uppercase letter")
    if not has_lower:
        missing.append("Lowercase letter")
    if not has_digit:
        missing.append("Digit")
    
    return is_valid, strength, missing

# Test enhanced checker
print("\nEnhanced password strength analysis:")

test_pwd = input("\nEnter password for strength analysis: ")
valid, strength, missing = check_password_strength(test_pwd)

print(f"\nPassword: {test_pwd}")
print(f"Valid: {valid}")
print(f"Strength: {strength}")

if missing:
    print(f"Missing: {', '.join(missing)}")
else:
    print("All basic requirements met!")


# Common password patterns to avoid
print("\n" + "=" * 80)
print("BONUS: Common Weak Patterns Detection")
print("=" * 80)

weak_patterns = ["12345", "password", "qwerty", "abc123", "admin", "letmein"]

check_pwd = input("\nEnter password to check for weak patterns: ")

is_weak = any(pattern in check_pwd.lower() for pattern in weak_patterns)

if is_weak:
    print("⚠ Warning: Password contains common weak patterns!")
else:
    print("✓ No common weak patterns detected.")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
