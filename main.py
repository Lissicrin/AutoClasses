class Transs:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.wheels = 4

        self.beep()
        self.about()


    def beep(self):
        print("bee")

    def about(self):
        print(f"Максимальная скорость: {self.speed}")
        print(f"Цвет вашего авто: {self.color}")

class Abobus(Transs):
    def __init__(self, speed, color, seats):
        self.seats = seats
        super().__init__(speed, color)
        self.wheels = 6

    def beep(self):
        print("baaav!")

    def about(self):
        print("Кто ты воин?: -Я автобус...>:3")
        super().about()
        print(f"Количество сидячих мест: {self.seats}")


car1 = Transs(200,"dark blue")
print(car1.speed)
car1.color = "red"
car1.about()

bus1 = Abobus(80,"blue", 32 )


