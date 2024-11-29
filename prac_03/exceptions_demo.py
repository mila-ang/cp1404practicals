"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When the user inputs something that cannot be converted into an integer, such as a string or special character.
2. When will a ZeroDivisionError occur?
When the user inputs 0 as the denominator, since division by zero is undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by adding a check before attempting the division to ensure the denominator is not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check if the denominator is zero before attempting the division
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Please enter a non-zero denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
