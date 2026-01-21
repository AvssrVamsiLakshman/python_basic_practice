# ============================================================
# AP 03: Grocery Bill Checker
# ============================================================
# Description: Calculate total cost of grocery items and display
#              the grand total along with spending limit.
# ============================================================

# Prompt user for Item 1 details
qty1 = float(input("Enter quantity for Item 1: "))
price1 = float(input("Enter unit price for Item 1: "))

# Prompt user for Item 2 details
qty2 = float(input("Enter quantity for Item 2: "))
price2 = float(input("Enter unit price for Item 2: "))

# Prompt user for spending limit
spending_limit = float(input("Enter your spending limit: "))

# Calculate totals
item1_total = qty1 * price1
item2_total = qty2 * price2
grand_total = item1_total + item2_total

# Display results
print("\n--- Grocery Bill Summary ---")
print("Item 1 Total:", item1_total)
print("Item 2 Total:", item2_total)
print("Grand Total:", grand_total)
print("Spending Limit:", spending_limit)
