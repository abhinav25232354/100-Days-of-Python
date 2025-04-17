# Break statement helps for breaking loop after a specific iteration
for i in range (12):
    print(i)
    i += 1
    if (i == 10):
        break
# Above loop will iterate till 9 and exit at 10

# continue statement is used to skip specific iteration from a loop
for i in range (12):
    if (i == 9):
        continue
    print(i)
    i += 1
# Above loop will iterate till 11 but will skip the 11th iteration