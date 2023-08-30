import datetime
from project import Project

MENU =\
    "- (L)oad projects\n" \
    "- (S)ave projects\n"\
    "- (D)isplay projects\n"\
    "- (F)ilter projects by date\n"\
    "- (A)dd new project\n"\
    "- (U)pdate project\n"\
    "- (Q)uit"


def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            data = line.strip().split('\t')
            project = Project(data[0], datetime.datetime.strptime(data[1], "%d/%m/%Y"),
                              int(data[2]), float(data[3]), int(data[4]))
            projects.append(project)
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")


def display_projects(projects):
    projects.sort()
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    filtered_projects = [project for project in projects if project.start_date > date]
    for project in filtered_projects:
        print(f"  {project}")


def add_new_project(projects):
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yyyy): "), "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("New project added.")


def update_project(projects):
    project_choice = int(input("Project choice: "))
    if 0 <= project_choice < len(projects):
        project = projects[project_choice]
        new_completion = int(input("New Percentage: "))
        new_priority = input("New Priority: ")

        if 0 <= new_completion <= 100:
            project.completion_percentage = new_completion
        if new_priority:
            project.priority = int(new_priority)

        print("Project updated.")
    else:
        print("Invalid project choice.")


def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    while True:

        print(MENU)

        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            if projects:
                print("load successful !!")
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
            if filename:
                print("save successful !!")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_string = input("Show projects that start after date (dd/mm/yyyy): ")
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y")
            filter_projects_by_date(projects, filter_date)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


main()
