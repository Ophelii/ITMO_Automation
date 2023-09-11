# Задание 2
def max_num(a:int, b:int):
    if a > b:
        print("Нaибольшее число ", a )
    elif b > a:
        print("Наибольшее число ", b )
    else:
        print('Введите неравные друг другу числа')

max_num(453, 328)

# Задание 3
def dif_num(num1:int, num2:int):

    if abs(num1 - num2) == 135:
        print('Yes')
    else:
        print('No')

dif_num(5, 147)

# Задание 4
def season(month):
    if 3 <= month <= 5:
        print('Это весна')
    elif 6 <= month <= 8:
        print('Это лето')
    elif 9 <= month <= 11:
        print('Это осень')
    else:
        print('Это зима')

season(8)

# Задание 5
def over_ten(num1, num2, num3):
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('Yes')
    else:
        print('No')

over_ten(777,14,11)

# Задание 6
def count_positive_num(list1):
    positive = 0
    for num in list1:
        if num > 0:
            positive += 1
    return positive

list1 = [4, -2, 55, -11, 5]
positive_count = count_positive_num(list1)
print('Положительных чисел в списке: ', positive_count)


# Задание 7
def days(year:int, month:int):
    total_days = year * 12 * 29 + month * 29
    print(f'{year} лет и {month} месяцев соответствуют  {total_days} дням')
days(5, 2)

