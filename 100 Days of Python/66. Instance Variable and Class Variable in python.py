# Instance variable is connected with Instance not class
class Employee:
    Raise_amount = 0.02 # Class Variable
    
    def __init__(self):
        self.name = "XYZ" # Instance Variable

emp1 = Employee() # Instance
print(emp1.name) # Instance Variable
print(Employee.Raise_amount) # Class Variable
emp1.Raise_amount = 5
print(emp1.Raise_amount)