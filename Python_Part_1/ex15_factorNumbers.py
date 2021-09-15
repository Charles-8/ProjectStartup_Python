number = int(input("Digite um número"))
factor = 1
while number > 0:
    number1 = number - 1
    factor = factor * number
    number = number - 1  # number -= 1

print(factor)
