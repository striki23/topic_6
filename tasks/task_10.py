ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")
print('Выберите алфавит:\n 1. Латинский,\n 2. Кириллица\n')

choice_alph = int(input('Введите номер алфавита: '))

if choice_alph not in (1, 2):
    print('Упс! Выбран неверный режим. Попробуйте ещё раз...')
else:

    if choice_alph == 1:
        vowels = ALPHABETS["en_vowels"]
        consonants = ALPHABETS["en_consonants"]
        hints = 'Введите букву латинского алфавита:'

    elif choice_alph == 2:
        vowels = ALPHABETS["ru_vowels"]
        consonants = ALPHABETS["ru_consonants"]
        hints = 'Введите букву кириллицы:'

    letter = input(hints).upper()

    if letter in vowels:
        print(f'{letter} - гласная буква!')
    elif letter in consonants:
        print(f'{letter} - согласная буква!')
    else:
        print('Упс! Неизвестная буква. Попробуйте другую!')
