# Программа выводит соответствующий текст
# в зависимости от введенного возраста пользователя

age = int(input('Введите свой возраст: '))

if 0 < age < 18:
    level_name = 'Инициации'
elif 18 <= age <= 30:
    level_name = 'Приключений'
elif 31 <= age <= 50:
    level_name = 'Мастерства'
elif 51 <= age <= 65:
    level_name = 'Мудрости'
elif age > 65:
    level_name = 'Легенд'
else:
    print('Ошибка!')

print(f'Вы находитесь на уровне "{level_name}"')
