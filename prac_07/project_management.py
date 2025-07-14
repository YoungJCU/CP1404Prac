from project import Project
import datetime

FILENAME = "projects.txt"


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for p in projects:
            print(
                f"{p.name}\t{p.start_date.strftime('%d/%m/%Y')}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percentage}",
                file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    completed = sorted([p for p in projects if p.is_complete()])
    print("Incomplete projects: ")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects: ")
    for p in completed:
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Show projects after a specific date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date >= filter_date], key=lambda p: p.start_date)
    for p in filtered:
        print(p)


def add_new_project():
    """Prompt user to create and return a new project."""
    print("Let's add a new project")
    name = input("Name: ")
    start = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    complete = int(input("Percent complete: "))
    return Project(name, start, priority, cost, complete)


def update_project(projects):
    """Update selected project's % complete and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    print(project)
    new_percent = input("New Percentage: ")
    new_priority = input("New Priority: ")
    project.update(new_percent, new_priority)


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()

    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save in ['yes', 'y']:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
