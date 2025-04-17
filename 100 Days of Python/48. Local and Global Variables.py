x = 5
y = 10
print(f"This is Global X: {x}")

def hello():
    global y
    x = 10
    # print(x)
    print(f"This is Local X {x}")
    print(f"This is Global Y: {y} Fetched from global keyword")

hello()