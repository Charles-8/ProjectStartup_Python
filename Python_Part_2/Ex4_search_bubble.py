n = [2, 6, 8, 89, 74, 45, 12, 78, 96, 85, 74, 14, 25, 36]
m = [2, 3, 1, 4, 5, 6, 7, 9, 15, 49, 26, 48, 47, 14, 36, 45]

def search(list, lucky_number):
    for i in range(len(list)):
        if list[i] == lucky_number:
            return (i)
    return False




def bubblesort_short(list):
    fim = len(list)
    for i in range(fim - 1, 0, -1):
        change = False
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                change = True
        if not change:
            return
    print(list)


print(search(n, 8))
bubblesort_short(n)


