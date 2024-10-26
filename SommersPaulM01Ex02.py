"""
Author: Paul Sommers
Date written: 10/26/2024
Assignment: Module 01 Programming Assignment Part 2
Short Desc: This program calculates the total cost of a meal purchased at a restaurant.
            It prompts the user for the cost of the food, calculates the tax, the tip, 
            and then displays the total cost.
"""

# Step 1: Prompt the user for the food cost
food_charge = float(input("Enter the cost of the food: "))

# Step 2: Calculate the sales tax (7% of the food cost)
sales_tax = food_charge * 0.07

# Step 3: Calculate the tip (18% of the total after tax)
total_with_tax = food_charge + sales_tax
tip = total_with_tax * 0.18

# Step 4: Calculate the total amount to be paid
total_amount = food_charge + sales_tax + tip

# Step 5: Display the results
print(f"Food charge: ${food_charge:.2f}")
print(f"Sales tax (7%): ${sales_tax:.2f}")
print(f"Tip (18% on total with tax): ${tip:.2f}")
print(f"Total amount to be paid: ${total_amount:.2f}")