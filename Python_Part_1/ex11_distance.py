import math
coordinate1x = int(input("Digite a cordenada x de partida"))
coordinate1y = int(input("Digite a cordenada y de partida"))

coordinate2x = int(input("Digite a cordenada x de destino"))
coordinate2y = int(input("Digite a cordenada y de partida"))

distance = math.sqrt((coordinate1x-coordinate2x)**2 + (coordinate1y-coordinate2y)**2 )

if distance >= 10:
    print("longe")
else:
    print("perto")
