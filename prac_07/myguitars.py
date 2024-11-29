"""
CP1404 - Practical
My Guitars
"""

import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row[0], int(row[1]), float(row[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def main():
    """Load guitars from file, sort by year, and display them."""
    guitars = load_guitars('guitars.csv')
    guitars.sort()

    print("Guitars sorted by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)


main()
