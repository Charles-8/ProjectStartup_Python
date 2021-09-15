#como criar e modificar arquivos:
price_cars = [66500, 78000, 85000, 125000]

#'r' usado somente para ler algo
# 'w usado somente para escrever algo'
# 'r+' usado para ler e escrever algo
# 'a' usado para acrescentar algo
with open ('car_price.txt', 'w') as file:
    for price in price_cars:
        file.write(str(price) + '\n')

with open('car_price.txt', 'a') as file:
       for price in price_cars:
           file.write(str(price) + '\n')

with open('car_price.txt', 'r') as file:
    for price in file:
        file.write(str(price) + '\n')



