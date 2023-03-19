# Задача №13. 
# Пользователь вводит число N (1 ≤ N ≤ 10). 
# Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество 
# идущих подряд положительных чисел.

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

from random import randint

n = int(input("Введите целое число от 1 до 10: "))
counter1 = 0
counter_max = 0
for _ in range(n):
    number = randint(-50, 50)
    print(number)
    if number > 0:
        counter1 += 1
    elif counter1 > counter_max:
        counter_max = counter1
        counter1 = 0
    else:
        counter1 = 0

if counter1 > counter_max:
    counter_max = counter1

print(f"Наибольшее количества идущих подряд положительных чисел = {counter_max}")