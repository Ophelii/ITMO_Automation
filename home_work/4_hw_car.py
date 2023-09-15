class Car:
    def __init__(self, color="", type="", year=""):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска: {my_car.year}")

    def set_type(self, type):
        self.type = type
        print(f"Тип автомобиля: {my_car.type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля: {my_car.color}")

my_car = Car()

my_car.start()
my_car.stop()
my_car.set_year(2023)
my_car.set_type("Седан")
my_car.set_color("Синий")



# другое решение

class Car:
    def __int__(self, c, t, y):
        self.c = c
        self.y = y

    def add_y(self, y_new):
        self.y = y_new