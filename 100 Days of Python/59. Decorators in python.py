# decorators - 
def greet(function):
    print("Good Morning")
    function()
    print("Thanks for Using this Function")
    return

def before_add_function(function):
    def newfunc(*args, **kwargs):
        print("Add Function")
        print(function(*args, **kwargs))
        print("Function Executed")
    return newfunc


@greet
def hello():
    print("Hello")

@before_add_function
def add(x, y):
    return x+y

add(2, 4)