
a = [11, 120, 300, 200, 2, 3, 4, 15, 1, 14, 11]

def remove_repeat(list_int):   #entre os parenteses nome do tipo do parametro que sera usado "neste caso uma LISTA" !
    b = []
    for number in list_int:
        if number not in b:    #Nesse exercício precisei usar o comando IN que verifica o que há ou não há NOT IN em uma lista
            b.append(number)   # lista.APENND(intem da lista) para adicionar um novo intem ao final de uma lista.
    b.sort()      #LISTA.SORT() comando para ordenar a lista de forma crescente.
    return b



print(remove_repeat(a))
