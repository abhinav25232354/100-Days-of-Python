# Exception handling using python
# Try Except Block or Statement

try:
    print("Hello world")
    a = 10
    print(a/0)

except ValueError:
    print("Number is not integer")

except IndexError:
    print("Index Error")
    
except Exception as e:
    print("Exception: ", e)

print("End of Program") # this line will executed even after exception execution