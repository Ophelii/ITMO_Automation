class A:
    def __init__(self):
        self.x = 10

...




class B(A):

    def __init__(self):
        super().__init__()
        self.y = self.x + 5

#  print(B().y)   # Мы еще не создали объект, но уже обращаемся к атрибуту (обращаемся к атрибуту y, когда его еще не ввели - это неверно

b = B()
print(b.y)