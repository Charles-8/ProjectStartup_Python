number = 0
while number >= 0:
    factor = 1
    number = int(input("Digite um número"))
    while number > 1:
        number1 = number - 1
        factor = factor * number
        number = number - 1  # number -= 1

    print(factor)
