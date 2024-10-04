"""
CP1404 - Practical
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# Get sales
sales = float(input("Enter sales: $"))

# Loop until the user enters a negative number
while sales >= 0:
    # Check and calculate
    if sales < 1000:
        bonus = sales * 0.10  # 10% bonus for sales under $1,000
    else:
        bonus = sales * 0.15  # 15% bonus for sales $1,000 or over

    # Print bonus
    print(f"Your bonus is: ${bonus:.2f}")

    # Get next input
    sales = float(input("Enter sales: $"))

print("Sales input ended. Goodbye!")
