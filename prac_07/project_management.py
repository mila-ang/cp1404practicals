"""
CP1404 - Practical
Project Management
Estimate: 1 hour
Actual:
"""

from datetime import datetime
from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (Q)uit"""


def main():
    """Run the main program loop."""
    projects = load_projects("projects.txt")
    print("Loaded projects from projects.txt")

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "L":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == "S":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "Q":
            print("Thank you for using the project management software.")
            break
        else:
            print("Invalid choice")


def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip the header
        for line in file:
            parts = line.strip().split('\t')
            project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
            projects.append(project)
    return projects


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda p: p.priority)
    completed = sorted([p for p in projects if p.is_complete()], key=lambda p: p.priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def save_projects(filename, projects):
    """Save a list of Project objects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate}\t{project.completion_percent}\n")


def filter_projects_by_date(projects):
    """Filter projects by a start date provided by the user."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
    filtered_projects = sorted([p for p in projects if p.matches_date(filter_date)],
                               key=lambda p: p.start_date)

    for project in filtered_projects:
        print(project)


main()
