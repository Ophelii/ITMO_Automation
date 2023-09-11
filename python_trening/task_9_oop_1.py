class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

search = Input('Input#search', 'ввод')

print(search.loc)

class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

reg = Button('Button#reg', 'Registration')

print(reg.loc)
print(reg.text)

class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

newtitle = Title('Title#newtitle', 'заголовок')

print(newtitle.loc)
print(newtitle.text)


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text

mylink = Link('Link#mylink', 'ссылка')

print(mylink.loc)
print(mylink.text)
