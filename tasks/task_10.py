ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")
print('Выберите алфавит:\n 1. Латинский,\n 2. Кириллица\n')

choice_alph = int(input('Введите номер алфавита: '))

# match choice_alph:
#     case 1:
#         choice_letter_l = input('Введите букву латинского алфавита: ').upper()
#         if choice_letter_l in ALPHABETS["en_vowels"]:
#             print(f'{choice_letter_l} - гласная буква!')
#         elif choice_letter_l in ALPHABETS["en_consonants"]:
#             print(f'{choice_letter_l} - согласная буква!')
#         else:
#             print('Упс! Неизвестная буква. Попробуйте другую!')
#     case 2:
#         choice_letter_k = input('Введите букву кириллицы: ').upper()
#         if choice_letter_k in ALPHABETS["ru_vowels"]:
#             print(f'{choice_letter_k} - гласная буква!')
#         elif choice_letter_k in ALPHABETS["ru_consonants"]:
#             print(f'{choice_letter_k} - согласная буква!')
#         else:
#             print('Упс! Неизвестная буква. Попробуйте другую!')
#     case _:
#         print('Упс! Выбран неверный режим. Попробуйте ещё раз...')

# ----------------------------

if choice_alph not in (1, 2):
    print('Упс! Выбран неверный режим. Попробуйте ещё раз...')
else:
    vowels = None
    consonants = None
    hints = None

    if choice_alph == 1:
        ...

    elif choice_alph == ...:
        ...

    choice_letter = input(hints)
    if choice_letter in vowels:
        print(f'{choice_letter} - гласная буква!')
    elif choice_letter in consonants:
        print(f'{choice_letter} - согласная буква!')
    else:
        print('Упс! Неизвестная буква. Попробуйте другую!')
