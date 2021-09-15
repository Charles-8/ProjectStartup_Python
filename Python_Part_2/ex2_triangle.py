class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c



    def calculate_perimeter(self):
        return "Perímetro", self.side_a + self.side_b + self.side_c

    def type_side(self):
        if self.side_a ** 3 == self.side_a * self.side_b * self.side_c:
            return "Esse Triangulo é equlátero"
        if self.side_a != self.side_b and self.side_a != self.side_c and self.side_b != self.side_c:
                return "Esse triangulo é escaleno"
        else:
            return "Esse triangulo é isóceles"


def main():
    triangle1 = Triangle(30, 30, 30)
    print(triangle1.calculate_perimeter())
    print(triangle1.type_side())

main()