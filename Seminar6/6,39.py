# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 

# Вывод:
#  3 3 2 12
# (каждое число вводится с новой строки)

from random import randint
num_1=int(input("Введите размер первого массива: "))
num_2=int(input("Введите размер второго массива: "))
array_1=[randint(1,10) for _ in range(num_1)]
array_2=[randint(1,10) for _ in range(num_2)]
result_array=[elem for elem in array_1 if elem not in array_2]
print(array_1)
print(array_2)
print(result_array)

