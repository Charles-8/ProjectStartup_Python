row = 1
column = 1

while row <= 10:
    while column <= 10:
        print(row * column, end = "\t")
        column = column + 1
    row = row + 1
    print()
    column = 1
