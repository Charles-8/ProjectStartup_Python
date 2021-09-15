number = int(input("Digite um numero inteiro"))

unit = number % 10
dozen = ((number - unit) // 10) % 10

print("O Dígito da dezena é ", dozen)
