a = [3, 10, 15, 1, 40, 100]
b = [1, 2, 3, 4, 5, 6]

def sort(list):
    # end_list = len(list)
    x = 0
    for i in list:
        if i < x:
            return False
        x = i
    return True




print(sort(a))


