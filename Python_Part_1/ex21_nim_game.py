def match():
     print("***Vamos começar o jogo !!*** ")
     n = int(input("Número total de peças: "))
     m = int(input("Número máximos de peças por rodada"))
     if n % (m + 1) == 0:
          c = 'pc'

          print("Computador começa")
     else:
          print("Voce começa")
          c = "eu"
     return n, m, c




def computer_chooses_move(n, m):
     #teste = n // (m + 1)
     #teste2 = n % (m + 1)
     if n % (m + 1)  == 0:
          pcs = n - (m + 1)
          print("Tirei ", pcs, " peças!! ")
          return n, m

     else:
          pcs = n - m
          print("Tieri", pcs,"  peças!! ")
          return n, m

def user_chooses_move(n, m):

    while True:
        usermove = int(input("Quantas peças você vai tirar ?"))
        if usermove > 0 and username <= m:
            n = n - usermove
            return n, m
        else:
            print("Valor inválido!!")


a = match()
if a[2] == "pc":
     computer_chooses_move(a[0], a[1])
else:
     user_chooses_move(a[0], a[1])
     print(user_chooses_move(a[0], a[1]))


