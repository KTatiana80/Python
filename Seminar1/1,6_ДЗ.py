# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

def Sum_of_three_digit_number(number):
    first_digit = number // 100
    second_digit = (number // 10) % 10
    third_digit = number % 10
    return first_digit + second_digit + third_digit


number = int(input("Введите номер билета "))
first_three_digit = number // 1000
last_three_digit = number % 1000
if Sum_of_three_digit_number(first_three_digit) == Sum_of_three_digit_number(last_three_digit):
    print("Ваш билет счастливый! :) ")
else:
    print("Билет не счастливый :( ")
