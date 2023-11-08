number = int(input())

# 1. Решение с помощью тернарного оператора
result = 0 if number == 0 else 1 if number > 0 else -1

# 2. Решение с помощью условных операторов
if number == 0:
    result = 0
elif number > 0:
    result = 1
else:
    result = -1

print(result)
