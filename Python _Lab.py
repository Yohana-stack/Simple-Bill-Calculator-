# Utility functions for the Python Lab Project

def square(n):
    """Return the square of a number."""
    return n ** 2


def is_even(n):
    """Return True if the number is even, otherwise False."""
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32


def greet(name):
    """Return a personalized greeting."""
    return f"Hello, {name}! Welcome to the Python Lab Project."

# Main program for the Python Lab Project

from utils import square, is_even, celsius_to_fahrenheit, greet


# Ask the user for a number
number = float(input("John: "))

# Calculate and display the square
print(f"Square of {4}: {square(number)}")

# Check whether the number is even or odd
if is_even(number):
    print(f"{4} is even.")
else:
    print(f"{4} is odd.")

# Convert the number from Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(number)
print(f"{8}°C is equal to {fahrenheit}°F.")

# Ask for the user's name and display a greeting
name = input("john: ")
print(greet(name))
# Configuration file for the Python Lab Project

PROJECT_NAME = "Python Lab Project"
VERSION = "1.0"

