"""
CP1404 - Practical
Files
"""

# Question 1:

name = input("Enter your name: ")

name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()

# Question 2:

name_file = open("name.txt", "r")
name_in_file = name_file.read().strip()
name_file.close()

print(f"Hi {name_in_file}!")

# Question 3
with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline())  # Read the first line and converting to int
    second_number = int(numbers_file.readline())  # Read the second line and converting to int

result = first_number + second_number
print(result)  # Should print 59

# Question 4

total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())

print(total)
