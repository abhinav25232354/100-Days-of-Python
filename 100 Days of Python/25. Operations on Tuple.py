# Only way to operae in tuple is to convert 
# tuple into list and then again convert it to tuple
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup1 = (11, 12, 13, 14, 15)
tuple1 = list(tup)
tuple2 = list(tup1)
tuple1.append(tuple2)
print(tuple1)
