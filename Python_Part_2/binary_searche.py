b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 45, 78, 41, 52, 63, 78, 13, 14, 15, 16, 17, 18, 19, 20, 365, 789, 56]

# Esse algorítimo faz uma busca por fatias, sempre divide a lista no meio, identifica em qual parte esta o elemento
# se o elemento estiver na primeira parte, a sgunda parte da lista é descartada, logo ele dividira em 2 partes a
# primeira parte novamente, e assim por diante ate chegar no elemento procurado.
#
def binary_search(list1, x):
    list1 = sorted(list1)     #sorted(list) função para ordenar uma lista
    first = 0
    last = len(list1) - 1
    while first <= last:
        middle = (first + last) // 2
        if list1[middle] == x:
            return middle
        else:
            if x < list1[middle]:
                last = middle - 1
                print(list1[middle])
            else:
                first = middle + 1

    print(list1)

    return -1


print(binary_search(b, 78))
