class Transs:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
        self.beep()
        self.about()

    def beep(self):
        print("bee")

    def about(self):
        print(f"Максимальная скорость: {self.speed}")
        print(f"Цвет вашего авто: {self.color}")

car1 = Transs(0.1,"dark blue")
print(car1.speed)