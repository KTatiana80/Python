# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

word = input("Введите слово: ").split()
my_dict = dict()

for letter in word:
    print(letter, end="")
    if letter not in my_dict:
        my_dict[letter] = 0
    else:
        my_dict[letter] += 1
        print("_", my_dict[letter], sep="", end="")
    print(end=" ")