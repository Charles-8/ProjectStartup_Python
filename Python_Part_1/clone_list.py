def clone(list):
    clone = []
    for object in list:
        clone.append(object)
        return clone
# a função clone, poder ser simplificada pelo seguinte comando "list[:]"
# exemplo:
fruit = ["aplee", "limon", "tometo", "orange"]

print(fruit)

fruit1 = fruit[:]

fruit1[0] = "Maça"

print(fruit1)
#Resumindo, para clonar uma lista para usar independentemente da lista que foi clonada, usamos [:]!!

if "aplee" in fruit:  #esse movimento se torna comum para testarmos uma lista e isso se chama PERTINENCIA a uma lista.
    print("Ai sim !!")

#CONCATENAÇÃO DE LISTAS
lista = [100, 200, 300]
concatenação_lista = [1, 2, 3, 4, 5] + lista  # esse movimento concatena 2 listas selecionadas !!

# OU

a = ["Charles", 32,]
b = ["Raul antonio da silva", 236, "villa verona"]

print(b + a)
print(a)
print(concatenação_lista)

#REPETIÇÃO DE LISTAS
# duplica a lista ou triplica e assim por diante representado por esse movimento !!
a = a * 3
print(a)

#REMOÇÃO EM LISTAS

#comando Del = Delete
del a[1]

print(a) #repare que ao rodar esse comando, o indice 1 da lista A foi apagado !!

#  E PARA APAGAR UMA FATIA DE UMA LISTA SEGUE EXEMPLO !!

cars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

del cars[3:7]  # ao rodar esse comando repare que na impreção a lista CARS vai estar com um pedaço apagado
# pois o comando [3:7] indica que os valores do indice 3 ao indice 7 serao apagados, lembrando que inclui o indice "3"
# e apagara ate o '6', sempre um a menos do que o indice informado.

print(cars)