class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_details(self):
        super().show_details()
        print("Employee ID:", self.employee_id)


class PartTime(Employee):
    def __init__(self, name, age, employee_id, working_hours):
        super().__init__(name, age, employee_id)
        self.working_hours = working_hours

    def show_details(self):
        super().show_details()
        print("Working Hours:", self.working_hours)


class Consultant(Person):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def show_details(self):
        super().show_details()
        print("Company:", self.company)


person = Person("Varsha", 30)

employee = Employee("Anu", 28, "E101")

parttime = PartTime("Meera", 25, "E102", 5)

consultant = Consultant("Rahul", 35, "ABC Company")


print("Person Details:")
person.show_details()

print("\nEmployee Details:")
employee.show_details()

print("\nPart-Time Details:")
parttime.show_details()

print("\nConsultant Details:")
consultant.show_details()