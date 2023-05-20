# Задание 1
from random import randrange
lst=[randrange(1,10) for i in range(int(input("Введите длинну массива ")))]
x=int(input('Введите число '))
a=0
for i in range(len(lst)):
    if lst[i]==x:
        a+=1
print(lst)
print("Ваше число встречается", a, "раз.")

# Задание 2

lst=[i for i in range(int(input("Введите длинну массива ")))]
x=int(input('Введите число '))
c=0
for i in lst:
    if abs(x-lst[i]) < abs(x-c):
        c=lst[i]
print(c)
print(lst)

# Задание 3

scrabble = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 's': 1, 't': 1, 'r': 1,
    'd': 2, "g": 2,
    'b': 3, 'c': 3, 'm': 3, 'p': 3,
    'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
    'k': 5,
    'j': 8, 'x': 8,
    "q":10, 'z': 10
}
sum = 0
lst=input("Введите слово ")
for i in lst:
    sum +=scrabble[i]
print(sum)

