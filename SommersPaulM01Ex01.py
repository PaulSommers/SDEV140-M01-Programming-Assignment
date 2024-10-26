"""
Author: Paul Sommers
Date written: 10/26/2024
Assignment: Module 01 Programming Assignment Part 1
Short Desc: This program converts a temperature from Celsius to Fahrenheit.
            The program prompts the user for a temperature in Celsius (float),
            converts it to Fahrenheit, and then displays the result.
"""

# Step 1: Prompt the user for the temperature in Celsius
celsius = float(input("Enter the temperature in Celsius: "))

# Step 2: Convert the Celsius temperature to Fahrenheit
# Formula: F = (9/5) * C + 32
fahrenheit = (9/5) * celsius + 32

# Step 3: Print the Fahrenheit temperature
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}°F")