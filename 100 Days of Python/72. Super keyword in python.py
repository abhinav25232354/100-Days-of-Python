# super keyword

class ParentClass:
    def __init__(self):
        pass
    def Parent_method(self):
        print("This is Parent Class")

class ChildClass(ParentClass):
    def Child_method(self):
        print("This is child class")
        super().Parent_method() # Parent method
        
child = ChildClass()
child.Child_method()