# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     sort_numbers(numbers)
#     display_numbers(numbers)
#
#
# def get_numbers():
#     numbers = input("Enter numbers separated by commas: ")
#     number_list = [float(num) for num in numbers.split(",")]
#     return number_list
#
#
# def square_numbers(numbers):
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i]**2
#
#
# def sort_numbers(numbers):
#     numbers.sort()
#
#
# def display_numbers(numbers):
#     for number in numbers:
#         print(f"{number}", end="..")
#     print()
#
#
# main()

data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantelle', 9]]

name_width = max((len(pair[0]) for pair in data))
score_width = max((len(str(pair[1])) for pair in data))

for pair in data:
    name, score = pair
    print(f"{name:{name_width}} = {score:{score_width}}")
print()


