# Пользователь вводит цвет
color = input('Введите ваш любимый цвет: ')

# Выводим тот или иной текст в зависимости от ответа пользователя
if color == 'солнечно-желтый' or color == 'небесно-голубой':
    print('Это цвет радости и счастья!')
else:
    print('Это тоже хороший цвет!')

# Вариант 2
if color in ('солнечно-желтый', 'небесно-голубой'):
    print('Это цвет радости и счастья!')
else:
    print('Это тоже хороший цвет!')
