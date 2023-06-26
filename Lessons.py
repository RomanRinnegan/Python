# # # Задание 1
# for i in range (1, 11):
#     for j in range (i, i*10, i):
#         print (j , end='\t')
#     print()
#
# # Задание 2
# a = int(input("Введите длинну стороны а :", ))
# b = int(input("Введите длинну стороны b :", ))
# c = int(input("Введите длинну стороны c :", ))
# if a + b > c and b + c > a and a + c > b:
#     print("Треугольник существует!")
#     if a == b == c:
#         print("Треугольник равносторонний!")
#     elif a == b or a == c or b == c:
#         print("Треугольние равнобедренный!")
#     else:
#         print("Треугольник разносторонний!")
# else:
#     print("Треугольник не существует!")
#
#
#
# # Задание 3
#
# num = int(input("Введите любое число от 0 до 100тыс.:", ))
# counter = 0
# for i in range(1, num+1):
#     if num % i == 0:
#         counter +=1
# if counter <= 2:
#     print("Число простое")
# else:
#     print("Число составное")
#
# print("Число делителей:", counter)

# Задание 4
from random import randint

num = randint(0, 1000)
guess = int(input("Угадайте загаданное число:", ))
counter = 0
while guess != num and counter < 11:
    if guess < num :
        guess = int(input("Мало! Нужно больше!:", ))
        counter += 1
    else:
        guess = int(input("Много! Нужно меньше!:", ))
        counter += 1
if guess == num:
    print(f'Ура! Вы угадали! ваше число: {guess}')
else:
    print(f'Cорян. Загаданное число было {num}')


