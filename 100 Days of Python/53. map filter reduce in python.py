# map function
# map - map(function, iterable)

def cube(x):
    return x**3

l = [1, 2, 3, 4, 5]
newl = []
for items in l:
    newl.append(cube(items))
print(cube(2))
print(newl)

# Now here is a shortcut for the whole cube of the list program
newl = list(map(cube, l))
print(newl)

# FILTER
# filter just do that it filters the elements which qualifies the criteria
# filter - filter(function, iterable)
def filter_function(a):
    return a>2
newnewl = filter(filter_function, l)
# newnewl = filter(1>2, l)
print(list(newnewl))

# Reduce
# reduce(function, iterable)
# Only two parameters in the function
from functools import reduce
def sum(a, b):
    return a+b

print(reduce(sum, l))