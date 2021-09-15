import random


class TimeCount:
    def randon_list(self, n):
        list = [0 for x in range(n)]
        for i in range(n):
            list[i] = random.randrange(1000) # comando para gerar numeros inteiros entre 0 e 999!
            return list

