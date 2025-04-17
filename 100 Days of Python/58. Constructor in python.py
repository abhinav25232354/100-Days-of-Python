# constructor in python def __init__
# it get called automatically whenever a object is created from the class
class Phone:
    def __init__(self, display, battery, price):
        self.display = display
        self.battery = battery
        self.price   = price
    def info(self):
        print(f"Display: {self.display}")
        print(f"Battery: {self.battery}")
        print(f"Price: {self.price}")

Xiaomi = Phone(6.1, 6000, 15000)
Xiaomi.info()