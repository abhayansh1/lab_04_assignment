class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.name}, {self.age} years old, Salary: ${self.salary}"

def sort_employees(employees, key):
    if key == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif key == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif key == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        return employees

def main():
    employees = [
        Employee("Raman", 41, 56000),
        Employee("Himadri", 38, 67500),
        Employee("Jaya", 51, 82100),
        Employee("Tejas", 30, 55000),
        Employee("Ajay", 45, 44000),1
    ]

    print("Sorting Options:")
    print("1. Sort by Age")
    print("2. Sort by Name")
    print("3. Sort by Salary")

    choice = int(input("Enter your choice (1/2/3): "))

    sorted_employees = sort_employees(employees, choice)

    print("\nSorted Employee Data:")
    for employee in sorted_employees:
        print(employee)

if __name__ == "__main__":
    main()
