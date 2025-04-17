# built-in class method by python
class Employee:
    company = "Apple"
    def show(self):
        print(f"{self.name} works in {self.company}")
    @classmethod
    def change_company(classs, new_company):
        classs.company = new_company
        # Classs.company is treated as instance variable

e1 = Employee()
e1.name = "Rames"
e1.show()
e1.change_company("Tesla")
e1.show()
print(Employee.company)

        