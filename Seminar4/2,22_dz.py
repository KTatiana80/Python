'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
import random

def fill_array(length):
    array = []
    i = 0
    while(i<length):
        array.append(random.randint(-length, length))
        i+=1
    return array

n = int(input('кол-во элементов первого множества: '))
m = int(input('кол-во элементов второго множества: '))
first_array = fill_array(n)
second_array = fill_array(m)
print(first_array)
print(second_array)

intersection = list(set(first_array) & set(second_array))
intersection.sort()

print(intersection if len(intersection) else 'Пересечений не найдено')