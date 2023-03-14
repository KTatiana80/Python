# Задача 2
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число "))
if number < 100 or number > 999:
    print(input("Введено не трех значное число "))
else:
    first_digit = number // 100
    second_digit = (number // 10) % 10
    third_digit = number % 10
    print(first_digit + second_digit + third_digit)
