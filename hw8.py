class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)

class Trainer(Employee):
    def __init__(self, name, role, specialization):
        super().__init__(name, role)
        self.specialization = specialization

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        
class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        super().__init__(name, role)
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Yoga Style:", self.yoga_style)

class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Employee.__init__(self, name, role)
        self.specialization = specialization
        self.yoga_style = yoga_style

    def display(self):
        print("Name:", self.name)
        print("Role:", self.role)
        print("Specialization:", self.specialization)
        print("Yoga Style:", self.yoga_style)
        
employee = Employee("Arun", "Manager")
trainer = Trainer("Rahul", "Trainer", "Strength Training")
yoga_instructor = YogaInstructor("Anjali", "Yoga Instructor", "Hatha Yoga")
multi_trainer = MultiTrainer(
    "Meera",
    "Multi Trainer",
    "Fitness Training",
    "Vinyasa Yoga"
)
print("Employee Details:")
employee.display()
print("\nTrainer Details:")
trainer.display()
print("\nYoga Instructor Details:")
yoga_instructor.display()
print("\nMulti Trainer Details:")
multi_trainer.display()