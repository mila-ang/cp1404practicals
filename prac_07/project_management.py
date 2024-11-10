"""
CP1404 - Practical
Project Management
Estimate: 1 hour
Actual:
"""

from project import Project


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
