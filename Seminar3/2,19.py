# Задача №19. 
# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения 
# списка или список задан изначально

"""
list_1=[]
for i in range(1, 6):
    list_1.append(i)
print(list_1)
k = int(input("Введите число: "))
for i in range(k):
    # temp = list_1[0]
    # print(list_1.pop(0))
    list_1.append(list_1.pop(0))
print()
print(list_1)
"""

"""
mas = [1, 2, 3, 4, 5]
k = int(input("k "))

for _ in range(k):
    mas.insert(0, mas.pop())
print(mas)
"""

list = [1, 2, 3, 4, 5]
k = 3

# temp = list[k:]
# list[k:] = list[:k]
# list[:k] = temp
# print(list)


##list[k:], list[:k] = list[:k], list[k:]
##print(list)
###print(list[:k] + list[k:])    почемуто не работает