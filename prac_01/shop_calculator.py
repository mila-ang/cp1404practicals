"""
CP1404 - Practical
Shop Calculator
"""

# Get and check user input for number of items
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Set total price to 0
total_price = 0

# Get price for each item and calculate total price
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

# Apply a 10% discount if the total price is over $100
if total_price > 100:
    total_price *= 0.9  # Apply a 10% discount

# Display the total price to 2 decimal places
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
