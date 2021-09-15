height = int(input("Digite a altura do Retangulo: "))
widht = int(input("Digite o largura do Retangulo "))
rectangle_height = 1
rectangle_widht = 1
while rectangle_height <= height:
    if rectangle_widht == rectangle_height or rectangle_widht == widht:
        print()
    print("#", end="\t")
    while rectangle_widht <= widht:
        rectangle_widht = rectangle_widht + 1
    rectangle_widht = 1
    print("#")
    rectangle_height = rectangle_height + 1

