# Base class
class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


# Derived class
class Manager(Employee):
    def __init__(self, name, age, salary, address, department):
        super().__init__(name, age, salary, address)
        self.department = department

    def display_manager(self):
        self.display()
        print("Department:", self.department)
        print("-------------------------")


# Process information of 10 managers
managers = []

for i in range(10):
    print(f"\nEnter details for Manager {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    address = input("Address: ")
    department = input("Department: ")

    m = Manager(name, age, salary, address, department)
    managers.append(m)

print("\n--- Manager Details ---\n")
for m in managers:
    m.display_manager()
