# Пользователь вводит три значения,
# если хотя бы одно значения истинно, выводится "Да"

number = int(input('Введите целое число: '))
fraction = float(input('Введите дробное число: '))
line = input('Введите строку: ')

lst = [bool(number), bool(fraction), bool(line)]
if True in lst:
    print('Да')
else:
    print('Нет')

# -------------------------------

if any((number, fraction, line)):
    print('Да')
else:
    print('Нет')
