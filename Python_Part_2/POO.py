
class Car:     # Nome de uma classe sempre tem que começar com letra maiuscula. para identificalas no code!

    def __init__(self, yer, model, color, speed, maxspeed):
        self.yer = yer
        self.model = model
        self.color = color
        self.speed = 0
        self.maxspeed = maxspeed #velocidade maxima

    def print_out(self):
        if self.speed == 0: # parado, da pra ver o ano!!
            print(f"{self.model} {self.color} {self.yer}")
        elif self.speed < self.maxspeed:
            print(f'{self.model} {self.color} indo a {self.speed}')
        else:
            print(f'{self.model} {self.color} indo muito raaaapiiiidooo!!!')


    def speed_up(self, speed):
        self.speed = speed
        if self.speed > self.maxspeed:
            self.speed = self.maxspeed
        self.print_out()

    def stop(self):
        self.speed = 0
        self.print_out()


def main():
    car_grandfather = Car(2021, "Civic", "White", 0, 240)
    my_car = Car(1994, "Monza", "Black", 0, 220)

    car1 = my_car
    car2 = car_grandfather

    car1.speed_up(40)
    car2.speed_up(50)

    car1.speed_up(140)
    car1.stop()
    car2.speed_up(250)


main()

renault = Car(2014, 'Sandero', 'prata', 120, 220)

renault.speed_up(200)




# class Pato:
#   pass
#
# pato = Pato()
# patinho = Pato()
# if pato == patinho:
#   print("Estamos no mesmo endereço!")
# else:
#   print("Estamos em endereços diferentes!")

