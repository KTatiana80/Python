# Задача №45.
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:       Вывод:
# 300         220 284


# def sum_del(num):
#     sum_a = 0
#     for el in range(1, num):
#         if num % el == 0:
#             sum_a += el
#     return sum_a


# k = int(input('введите k: '))
# for first_num in range(1, k):
#     second_num = sum_del(first_num)
#     if sum_del(second_num) == first_num and first_num != second_num and first_num > second_num:
#         print(first_num, second_num)


def sum_del(num):
    sum_a = 1
    for el in range(2, int(num**0.5 + 1)):
        if num % el == 0:
            sum_a += el + num // el
    return sum_a


k = int(input('введите k: '))
for first_num in range(1, k):
    second_num = sum_del(first_num)
    if sum_del(second_num) == first_num and first_num != second_num and first_num > second_num:
        print(first_num, second_num)