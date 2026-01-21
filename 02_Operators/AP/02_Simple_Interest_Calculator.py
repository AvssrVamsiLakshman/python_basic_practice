# ============================================================
# AP 02: Simple Interest Calculator
# ============================================================
# Description: Calculate simple interest using the formula
#              Simple Interest = (Principal × Rate × Time) / 100
# ============================================================

# Take input from user for principal, rate and time
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time period (in years): "))

# Calculate simple interest using the formula
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest
print("\n--- Simple Interest Calculator ---")
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time Period:", time, "years")
print("Simple Interest:", simple_interest)
