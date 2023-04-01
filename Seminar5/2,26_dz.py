'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

def recursive_pow(a,b):
    if b>0:
        return a*recursive_pow(a,b-1)
    return 1

a = int(input('число A: '))
b = int(input('число B: '))
result = recursive_pow(a,b)
print(f'число {a} в степени {b} = {result}')