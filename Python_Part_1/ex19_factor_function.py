# FUNÇÕES
# Nesse Exercício, guardo uma função dentro de outra para economizar linhas de codigo
# e facilitar a correção de erros.

#n = int(input("Digite o valor de n"))
#k = int(input("Digite o valor de n"))


def factors(n):  # Função em que guardo a logica para fatorar um numero inteiro.
    factor = 1
    while n > 0:
        number1 = n - 1
        factor = factor * n
        n = n - 1  # n -= 1

    return factor


def binomial_number(n,k):  # Função em que uso a fórmula para achar um número binomial (parcial)

    nk = factors(n) / (factors(k) * factors(n - k))

    return nk



# factors(n)
# factors(k)
print(binomial_number(3, 3))


