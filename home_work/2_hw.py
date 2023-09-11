def task_1(a: int, b: float, c: str, d: list, e: bool) -> None:
    print(a, "относится к типу ", type(a))
    print(b, "относится к типу ", type(b))
    print(c, "относится к типу ", type(c))
    print(d, "относится к типу ", type(d))
    print(e, "относится к типу ", type(e))


task_1(a=8, b=5.25, c='шар', d=[1, 25, 50, 175], e=False)

# Пследовательность чисел, используемая в списке - последовательность Фибоначчи


def task_2(a: list = [1, 2, 3, 5, 8, 13, 21]) -> list:
    print("Первые три значения списка: ", a[0:3])


task_2()


def task_3(x: int) -> int:
    return x ** 2


print("Квадрат числа равен ", task_3(5))
