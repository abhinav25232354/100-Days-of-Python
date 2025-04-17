# Classes are blueprint or template on which object are defined
class Railway_Form:
    def __init__(self, name1, age, price):
        self.name1 = name1
        self.age = age
        self.price = price
    def print_details(self):
        print(f"Name : {self.name1}")
        print(f"Age  : {self.age}")
        print(f"Price: {self.price}")

abhinav = Railway_Form("Abhinav", 18, 50000)
tom = Railway_Form("Tom", 16, 24000)
print(abhinav.print_details())
print(tom.print_details())