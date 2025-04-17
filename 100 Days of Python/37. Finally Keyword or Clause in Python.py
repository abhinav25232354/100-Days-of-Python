# Finally keyword used for executing exception block of code
try:
    l = [1, 2, 3, 4, 5]    
    i = input("Enter Index: ")
    print(l[i])
    # return 1
except:
    print("Index out of Range")
    # return 0

print("I am always Executed")

# Above works as finally but only in open code not in function
def ErrorReturningFunction():
    try:
        l = [1, 2, 3, 4, 5]    
        i = input("Enter Index: ")
        print(l[i])
        return 1
    except:
        print("Index out of Range")
        return 0
    
    finally:
        print("I am always Executed")

x = ErrorReturningFunction()
print(f"Function Returned: {x}")