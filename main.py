"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here
charge = 0.00  # Charge for this sign
numChars = 8   # Number of characters
color = "gold" # Color of characters
woodType = "oak"  # Type of wood
numChars = int(input("Enter the number of characters: "))
color = input("Enter the color of characters (gold/black/white): ")
woodType = input("Enter the wood type (oak/pine): ")

# Calculate the charge based on the given conditions
# Minimum charge starts at $35.00
charge = 35.00

# Calculate additional character charges
# First 5 characters are free, charge $4 for each additional character
if numChars > 5:
    charge += (numChars - 5) * 4

# Add wood type charge
if woodType == "oak":
    charge += 20.00

# Add color charge for gold-leaf lettering
if color == "gold":
    charge += 15.00

# Output Charge for this sign
print(f"The charge for this sign is ${charge:.2f}")