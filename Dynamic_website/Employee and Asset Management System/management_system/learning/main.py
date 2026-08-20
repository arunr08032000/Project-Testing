employees = []

def add_employee():
    name = input("enter name:")
    employees.append(name)
    print("employee added")

def view_employee():
    if len(employees) == 0:
        print("Employee not found")

    else:

        for employee in employees:
            print(employee)

def search_emloyee():
    name = input("Enter employee name")
    if name in employees:
        print("Employee founded")
        print(employees)
    else:
        print("Employee not found")

def delete_employee():
    name = input("Delete name")

    if name in employees:
        employees.remove(name)
        print("deleted")
    else:
        print("Employee not found")

def count_employee():
    print("Total Employees:", len(employees))

while True:
    print("\n============employee management===========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete employee")
    print("5. Total count")
    print("6. Exit")

    choise = int(input("Enter the options"))

    if choise == 1:
        add_employee()
    elif choise == 2:
        view_employee()
    elif choise == 3:
        search_emloyee()
    elif choise == 4:
        delete_employee()
    elif choise == 5:
        count_employee()
    elif choise == 6:
        print("bye")
        break
    else:
        print("invailed option")
    