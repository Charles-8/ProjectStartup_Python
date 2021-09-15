def create_matrice(line_numbers, column_numbers):
#(int, int) -> matriz (lista de lista)
#  Cria e teotrna uma matriz com num_linhas linhas e num_colunas colunas em que cada elemento é digitado pelo usuario!!
    matrice = []

    for i in range(line_numbers):
        line = []
        for j in range(column_numbers):
                value = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
                line.append(value) #add valor a "line"
        matrice.append(line) # add linha a matriz!


    return matrice


def read_matrice():
    line = int(input("Digite o numeros de linhas que tera a Matriz:  "))
    column = int(input("Digite o numero de colunas que tera sua Matriz: "))
    print(create_matrice(line, column))


read_matrice()
