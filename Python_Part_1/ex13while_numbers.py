number = 1
number1=0
adjacentnumber= False
while number1 != number % 10:
    number= int(input("Digite um numero inteiro"))
    number1= number % 10
    number= number // 10
if number1 == number % 10:
        adjacentnumber=True
if adjacentnumber:
    print("Ai tem numeros iguais")




