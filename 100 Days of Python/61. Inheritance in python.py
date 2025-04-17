# Making a new class with the previous properties of parent class

class Employee:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age
    def show_details(self):
        print(f"ID: {self.id}\nName: {self.name}\nAge: {self.age}")

class Extended_Employee(Employee):
    def show_language(self):
        print("Default Language is Python")
        
e1 = Employee(101, "Pappu", 36)
e1.show_details()
e2 = Extended_Employee(101, "Pappu", 36)
e2.show_details()
e2.show_language()