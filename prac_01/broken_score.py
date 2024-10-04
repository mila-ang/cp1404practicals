"""
CP1404 - Practical
Program to determine score status
"""

# Get user score
score = float(input("Enter score: "))

# Check for valid score
if score < 0 or score > 100:
    print("Invalid score")
# Determine excellent, passable, bad
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
