# Задание 1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # S = w * h
    def area(self):
        s_rec = self.width * self.height
        print(f'Площадь прямоугольника равна {s_rec}')

    # P = 2(w+h)
    def perim(self):
        p_rec = 2 * (self.width + self.height)
        print(f'Периметр прямоугольника равен {p_rec}')

object1 = Rectangle(6, 9)
object2 = Rectangle(1, 3)
object3 = Rectangle(4, 4)

object1.area()
object2.area()
object3.area()

print('\n')

object1.perim()
object2.perim()
object3.perim()


print('\n')
print('\n')

# Задание 2
class Math:

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def addition(self):
        add = self.a + self.b
        print(f'Результат сложения {self.a} и {self.b} равен: {add}')

    def multiplication(self):
        mult = self.a * self.b
        print(f'Результат умножения {self.a} и {self.b} равен: {mult}')

    def devision(self):
        dev = self.a / self.b
        print(f'Результат деления {self.a} и {self.b} равен: {dev}')

    def subtraction(self):
        sub = self.a - self.b
        print(f'Результат вычитания {self.a} и {self.b} равен: {sub}')

math_par = Math(12, 3)

math_par.addition()
math_par.multiplication()
math_par.devision()
math_par.subtraction()

print('\n')
print('\n')


# Задание 3

class Sidebar:
    def __init__(self, text, loc = " "):
        self.text = text
        self.type = "Кнопка"
        self.loc = loc

    def click(self):
        return f"Клик по кнопке {self.text}"


text_box = Sidebar('Text box')
check_box = Sidebar('Check Box')
radio_button = Sidebar('Radio Button')
web_tables = Sidebar('Web tables')
buttons = Sidebar('Buttons')
links = Sidebar('Links')
broken_links = Sidebar('Broken Links - Images')
upl_downl = Sidebar('Upload and Download')
dyn_prop = Sidebar('Dynamic Properties')

# Вывод текста для каждой кнопки
print(text_box.text)
print(check_box.text)
print(radio_button.text)
print(web_tables.text)
print(buttons.text)
print(links.text)
print(broken_links.text)
print(upl_downl.text)
print(dyn_prop.text)

# Клик для каждой кнопки
print(text_box.click())
print(check_box.click())
print(radio_button.click())
print(web_tables.click())
print(buttons.click())
print(links.click())
print(broken_links.click())
print(upl_downl.click())
print(dyn_prop.click())







