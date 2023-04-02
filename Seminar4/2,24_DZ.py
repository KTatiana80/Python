'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
# import random

# def fill_array(length, min, max):
#     array = []
#     i = 0
#     while(i<length):
#         array.append(random.randint(min, max))
#         i+=1
#     return array

# def find_max_harvest_siblings(array):
#     sum = 0
#     index = 0
#     for i in range(len(array)):
#         lerft_index = i-1 if i>0 else len(array)-1
#         right_index = i+1 if i<len(array)-1 else 0
#         current_sum = array[lerft_index]+array[i]+array[right_index]
#         if sum<current_sum:
#             sum = current_sum
#             index = i+1
#     return [sum, index]

# n = int(input('кол-во кустов: '))
# garden_bed = fill_array(n, 2, 10)
# print(garden_bed)
# [harvest, bush] = find_max_harvest_siblings(garden_bed)
# print(f'Максимальный урожай у куста {bush} число ягод {harvest}')


from random import randint
var_n = int(input("Введите число кустов: "))
list_berry = []
for i in range(var_n):
  list_berry.append(randint(5, 20))
print(list_berry)
sum_berry = [list_berry[i] + list_berry[i+1] + list_berry[i+2]
             for i in range(-2, len(list_berry) - 2)]
print(sum_berry)
max_berry = max(sum_berry)
print(f"Наибольшее число:", max_berry)