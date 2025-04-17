class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    # Using Class Method as alternative constructor
    @classmethod
    def fromstr(clas, string):
        return clas(string.split("-")[0], string.split("-")[1])

e1 = Employee("Pappu", 34000)
print(e1.name)
print(e1.salary)

string = "Ramesh-28000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
