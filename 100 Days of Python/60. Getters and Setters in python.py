# getters and setters
class getter:
    def __init__(self, value):
        self.value = value
    
    @property
    def into10(self):
        return self.value*10
    @into10.setter
    def into10(self, newvalue):
        self.value = newvalue/10

add = getter(3)
print(add.into10) # This is a getter (Getting a value after modification at runtime)
add.into10 = 50
print(add.into10)

# setter
