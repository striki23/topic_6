# Пользователь вводит три значения, если все значения истинны, выводится "Да"

number = int(input('Введите целое число: '))
fraction = float(input('Введите дробное число: '))
line = input('Введите строку: ')

if bool(number) == bool(fraction) == bool(line) is True:
    print('Да')
else:
    print('Нет')
