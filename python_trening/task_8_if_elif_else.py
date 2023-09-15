num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num_float > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


# Задача 1
course_num = 7

if 1 <= course_num <= 4:
    print('Бакалавр')
elif 5 <= course_num <= 6:
    print('Магистр')
elif 7 <= course_num <= 9:
    print('Аспирант')
else:
    print('Введите корректный год обучения')

# Задача 2
some_num = 888

if some_num > 100 or some_num < -100:
    print('-')
else:
    print('+')
