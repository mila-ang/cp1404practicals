"""
CP1404 - Practical
Hex Colors
"""

# Dictionary of color names and their hexadecimal values
COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

color_name = input("Enter color name: ").title()
while color_name != "":
    if color_name in COLOR_CODES:
        print(f"{color_name} is {COLOR_CODES[color_name]}")
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()
