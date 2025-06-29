# These are custom methods used for redefining the meaning of built-in function

class Student:
    def __init__(self):
        self.hello = "Hello"
    
    def __str__(self):
        return f"The Object is Saying {self.hello}"
    
stu = Student()
print(stu.__str__())