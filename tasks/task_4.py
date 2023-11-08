# Программа находит наибольшее число из трех введенных пользователем
# Если все числа равны, выводится сообщение 'Все числа равны'

num_1 = int(input('Введите первое целое число: '))
num_2 = int(input('Введите второе целое число: '))
num_3 = int(input('Введите третье целое число: '))

if num_1 == num_2 and num_3 == num_1:
    print('Все числа равны')
else:
    if num_1 >= num_2:
        if num_1 > num_3:
            max_num = num_1
        else:
            max_num = num_3
    else:
        if num_2 >= num_3:
            max_num = num_2
        else:
            max_num = num_3

    print('Наибольшее число:', max_num)

# ----------------

if num_1 == num_2 == num_3:
    print('Все числа равны')
elif num_1 > num_2 > num_3:
    print('Наибольшее число:', num_1)
elif num_2 > num_3:
    print('Наибольшее число:', num_2)
else:
    print('Наибольшее число:', num_3)
