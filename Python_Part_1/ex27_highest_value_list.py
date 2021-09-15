int = [7000, 10000, 3, 5000]

def highest_value(list_int):
    highest = 0
    for i in list_int:

        # for hi in list_int:

            if i >= highest:
                highest = i

    return highest

print(highest_value(int))



