class Button:
    type: str = 'Кнопка'

    def __init__(self, text, link):
        self.text = text
        self.link = link

# Создаем экземпляры класса
home = Button('Домой', "/home")
catalog_msk = Button('Каталог', '/msk/catalog')

# Получаем доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')
print(home.type)
print(catalog_msk.type)

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)  # в {} скобках помещаются переменные внутри строки, перечисление нужных переменных идет после, через запятую (это альтернативное написание конкатенации стро)

# Создаем экземпляр класса
home_two = ButtonTwo('Домой', "/home", "button#home")

# Вызываем метод
print(home_two.click())

#  Надо знать: класс объект метод атрибут
# Надо знать:  
# Надо знать: как создаются методы и атрибуты (объекты создаются строго внутри класса)