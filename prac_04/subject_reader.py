"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    print(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []  # Create an empty list to store the data

    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()  # Remove the \n at the end of each line
            parts = line.split(',')  # Separate the data into its parts
            parts[2] = int(parts[2])  # Convert the number of students to an integer
            data_list.append(parts)  # Append the processed line (list) to the main list

    return data_list  # Return the list of lists


main()
