int = [2, 3, 3, 2, 1, 4]


def sum_elements(lis):
    # x = sorted(lis)


    if len(lis) - 1 == lis[0:]:
        return 1
    else:
        return lis + (sum_elements(lis))





























































































































print(sum_elements(int))

# int = [2, 3, 3, 2, 1, 4]

# def sum_elements(list_int):
#     sum_i = 0
#
#     for i in list_int:
#         sum_i = sum_i + i
#     return  sum_i





