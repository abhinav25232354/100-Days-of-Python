# When we want to override method of parent class in child class

class Animal:
    def __init__(self, name):
        self.__name = name
    
    def getName(self):
        return f"Name: {self.__name}"
    
class Elephant(Animal):
    def __init__(self, ename):
        self.__ename = ename
        
    def getName(self):
        return f"Elephant Name: {self.__ename}"

a = Animal("Cat")
b = Elephant("Sheru")
print(a.getName())
print(b.getName())