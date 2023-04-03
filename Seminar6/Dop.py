# Списки
# map(int,input().split()) - метод split разбивает строку по пробелу,
# а map применяет указанную функцию к каждому элементу последовательности.
# [int(i) for i in input().split()] - второй способ создания списка
# *a - раскрывание итерируемого объекта

# list(map(int,input().split())) - список чисел

# a = '1 2 3 4 5 9'
# print(a.split())
# print(a.split(' '))
# print(a.split(' 4 '))
# nums = [int(i) for i in input('введиите чиисла через пробел').split()]
# print(nums)

# nums_2 = list(map(int,input('введиите чиисла через пробел').split()))
# print(nums_2)
# Ввод 7 2 5
# a, b, x = list(map(int,input('введиите чиисла через пробел').split()))
# a, b, x = int(input()), int(input()), int(input())
# print(a)
# print(b)
# print(x)

a,*b, x = (12,23,34,45,56,67)
print(a)
print(b)
print(x)

for a,*b,x in [(1,2,3, 4, 45), (11,22,33), (111,222,333)]:
    print(a,b,x)
for a in [(1,2,3, 4, 45), (11,22,33), (111,222,333)]:
    print(a)


# for *a in [45,33, 111]: # будет ошибка
#     print(a)