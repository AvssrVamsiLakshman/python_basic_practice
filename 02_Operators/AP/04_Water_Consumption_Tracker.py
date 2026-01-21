# ============================================================
# AP 04: Water Consumption Tracker
# ============================================================
# Description: Track water consumption over 3 days, calculate
#              average and display recommended limit.
# ============================================================

# Prompt user for water consumption for each day
day1 = float(input("Enter water consumed on Day 1 (in liters): "))
day2 = float(input("Enter water consumed on Day 2 (in liters): "))
day3 = float(input("Enter water consumed on Day 3 (in liters): "))

# Prompt user for recommended daily water intake
recommended = float(input("Enter recommended daily water intake (in liters): "))

# Calculate average water consumption
average_consumption = (day1 + day2 + day3) / 3

# Display results
print("\n--- Water Consumption Summary ---")
print("Average Daily Consumption:", average_consumption, "liters")
print("Recommended Limit:", recommended, "liters")
