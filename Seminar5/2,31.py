# Задача 31
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    list_1 = []
    for i in range(n):
        if i < 2:
            list_1.append(i)
    else:
        c = list_1[i-1] + list_1[i-2]
        list_1.append(c)
    print(list_1[n-1])

num = int(input('введите число: '))
fib(num)
