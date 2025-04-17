# dir, __dict__ and help method in python
# dir - can be used for searching how many attributes and methods can be applied to this
x = [1, 2, 3]
print(dir(x))
print(x.count(2)) # how many times a value is iterated inside the list object


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
s1 = Student("Ram Khelawan", 23)
print(s1.name)
print(s1.age)
print(s1.__dict__) # Returns the value setted with object in the form of dictionary

s2 = Student("Ram Mungeri", 21)
print(s2.__dict__)

# help
print(help(Student)) # Shows full documentation related to a object (any object)