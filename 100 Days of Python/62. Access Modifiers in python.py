"""
Public - Every object of a class is by default public and can be accessed from outside of the class
Private(__varname) - Cannot be accessed directly from outside the class but can be accessed outside the class with prefixing private object name with _classname
protected(_varname) - Can be used without changing values
"""

class access_modifiers:
    def __init__(self):
        self.name = "Public"
        self.__name2 = "Private"
        self._name3 = "Protected"
        
e1 = access_modifiers()
print(e1.name)
# print(e1.__name) # Throw error because of private
print(e1._access_modifiers__name2) # Accessed indirectly (Name Mangling)
print(e1._name3)