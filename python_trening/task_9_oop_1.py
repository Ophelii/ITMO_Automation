
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
        self.loc = locGIT MERGE
        self.text = text

mylink = Link('Link#mylink', 'ссылка')

print(mylink.loc)
print(mylink.text)

from task_9_checks import Checks

class Input(Checks):
    def init(self, loc, text):
        super().init(loc)
        self.text = text

class Button(Checks):
    def init(self, loc, text):
        super().init(loc)
        self.text = text

class Title(Checks):
    def init(self, loc, text):
        super().init(loc)
        self.text = text

class Link(Checks):
    def init(self, loc, text):
        super().init(loc)
        self.text = text

search = Input('Input#search', 'ввод')
reg = Button('Button#reg', 'Registration')
newtitle = Title('Title#newtitle', 'заголовок')
mylink = Link('Link#mylink', 'ссылка')



print(search.check_text())
print(reg.check_text())
print(newtitle.check_text())
print(mylink.check_text())