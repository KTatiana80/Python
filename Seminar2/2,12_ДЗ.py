# Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числаX и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 2) Пользователь вводит два числа построчно, первое – сумма двух чисел, 
# второе – произведение этих чисел. Нужно вывести исходные числа.

# 4 4 -> 2 2
# 5 6 -> 2 3
"""
def search(s,p):
    for i in range(s):
        for j in range(p):
            if i + j == s:
                if i * j == p:
                    print(i, j)
                    return 0
    return -1


def main():
    s = int(input("Введите первое число "))
    p = int(input("Введите второе число "))
    result = search(s,p)
    if(result == -1):
        print("Введены некорректные значения")

if __name__ == '__main__':
    main()
"""

my_sum = int(input("Summ = "))
my_przv = int(input("Composition = "))
for first in range(1, my_sum // 2+1):
    second = my_sum - first
    if my_przv == first * second:
        print(first, second)
        break
else:print("Введены нокорректные данные")