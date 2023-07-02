#Задание 1
"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата"""

# num = int(input('Число:', ))
#
# result_hex = ""
# h = '0123456789ABCDEF'
# num_for_hex = num
# while num_for_hex > 0:
#     result_hex += h[num_for_hex % 16]
#     num_for_hex //= 16
#
# result_hex = result_hex[::-1]
# print(result_hex, hex(num))

# Задание 2

"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions."""

import math

a = input("Напишите дробь со знаком деления '/':", ).split('/')
b = input("Напишите дробь со знаком деления '/':", ).split('/')
sum_numerator = f'{int(a[0]) + int(b[0])}'
sum_denominator = f'{int(a[1]) + int(b[1])}'
res_sum = f'Результат сложения: {sum_numerator} / {sum_denominator}'

mult_numerator = int(f'{int(a[0]) * int(b[0])}')
mult_denominator = int(f'{int(a[1]) * int(b[1])}')
c = math.gcd(mult_numerator, mult_denominator)
if mult_numerator % c == 0:
    mult_numerator = mult_numerator // c
else:
    mult_numerator = mult_numerator
if mult_denominator % c == 0:
    mult_denominator = mult_denominator // c
else:
    mult_denominator = mult_denominator
res_mult = f'Результат произведения: {mult_numerator} / {mult_denominator}'

print(res_sum, res_mult)



