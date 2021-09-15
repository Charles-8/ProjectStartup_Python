number = int(input("Digite um numero inteiro"))
number1 = 1
number2 = 0
sum = 0
while number1 != 0:
    number1 = number % 10
    number = number // 10
    sum = sum + number1
print(sum)







