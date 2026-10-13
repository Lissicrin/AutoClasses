class Transs:
    def __init__(self, speed, color, wheels = 4):
        self.speed = speed
        self.color = color
        self.wheels = wheels

        self.beep()
        self.about()
        self.hot_wheels()


    def beep(self):
        print("bee")

    def about(self):
        print(f"Максимальная скорость: {self.speed}")
        print(f"Цвет вашего авто: {self.color}")

    def hot_wheels(self):
        print(f"Количество колесиков тута {self.wheels}")

class Abobus(Transs):
    def __init__(self, speed, color, seats, wheels):
        self.seats = seats
        super().__init__(speed, color, wheels)


    def beep(self):
        print("baaav!")

    def about(self):
        print("Кто ты воин?: -Я автобус...>:3")
        super().about()
        print(f"Количество сидячих мест: {self.seats}")

    def seats(self):
        print(f"Посадочный мест тута {self.seats}")

car1 = Transs(200,"dark blue")
print(car1.speed)
car1.color = "red"
car1.about()

bus1 = Abobus(80,"blue", 32, 4 )
aurus = Abobus(10,"white",100, 10)





