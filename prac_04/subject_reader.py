"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load data and display subject details."""
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject, lecturer, number of students."""
    data_list = []  # Create an empty list to store the data

    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data_list.append(parts)

    return data_list  # Return the list of lists


def display_subject_details(data):
    """Display details of each subject in the required format."""
    for subject in data:
        subject_code = subject[0]
        lecturer = subject[1]
        number_of_students = subject[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students")


main()

