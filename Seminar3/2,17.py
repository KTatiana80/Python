# Задача №17. 
# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.

from random import randint
# list_1 =[]
# for _ in range(randint(5, 15)):
#     number = randint(-10, 10)
#     print(number, end = " ")
#     list_1.append(number)
list_1 =  [randint(-10, 10) for _ in range(randint(5, 15))]
print(list_1)
set_1=set(list_1)  
print()
print(len(set_1))



