from python_trening.task_9_oop_1 import Input

class Checks(Input):
    def __init__(self, loc):
        self.loc = loc

    def check_text(self):
        return self.loc

    def __init__(self, loc):
        super().__init__(loc)















# Создаем подклассы, которые наследуют Checks
class Subclass1(Checks):
    def __init__(self, loc, attr1):
        super().__init__(loc)
        self.attr1 = attr1

class Subclass2(Checks):
    def __init__(self, loc, attr2):
        super().__init__(loc)
        self.attr2 = attr2

class Subclass3(Checks):
    def __init__(self, loc, attr3):
        super().__init__(loc)
        self.attr3 = attr3

class Subclass4(Checks):
    def __init__(self, loc, attr4):
        super().__init__(loc)
        self.attr4 = attr4

# Создаем объекты
obj1 = Subclass1("Location 1", "Attribute 1")
obj2 = Subclass2("Location 2", "Attribute 2")
obj3 = Subclass3("Location 3", "Attribute 3")
obj4 = Subclass4("Location 4", "Attribute 4")

# Распечатываем результаты метода check_text() для каждого объекта
print(obj1.check_text())  # Выводит "Location 1"
print(obj2.check_text())  # Выводит "Location 2"
print(obj3.check_text())  # Выводит "Location 3"
print(obj4.check_text())  # Выводит "Location 4"