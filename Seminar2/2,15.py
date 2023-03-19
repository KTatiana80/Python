# Задача №15:
# Пользователь вводит одно число N. Далее идут N чисел, 
# записанных на новой строчке каждое. 
# Вывести максимальное и минимальное (циклы)

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

n = int(input("Введите целое число "))
min_num = 20
max_num = 0
for _ in range(n):
    number = randint(1, 20)
    print(number)
    if number < min_num:
        min_num = number
    if number > max_num:
        max_num = number
print(F"Минимальное число = {min_num}, максимальное число = {max_num}")
