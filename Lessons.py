# Задание № 1

a = int(input("Введите члюбое целое число: "))
b = float(input("Введите любое дробное число: "))
word = input("Введите любую фразу: ")
print("Ваше число:", a)
print("Ваше дробное число:", b)
print("Ваша фраза:", word)

name = input("Введите ваше имя: ")
password = input("Введите пароль: ")
age = int(input("Укажите ваш возраст: "))
print("Ваши данные для входа в аккаунт:", "имя -", name, "пароль -", password, "возраст -", age)

# Задание № 2

seconds = int(input("Введите количество секунд:"))
hour = seconds//3600
seconds %= 3600
minutes = seconds//60
seconds %= 60

print(f'{hour:02}', ":", f'{min:02}', ":", f'{seconds:02}')

# Задание №3


n = int(input("Введите целое число:"))
print(str(n)+str(2*n)+str(3*n))

print(f'{hour:02}', ":", f'{minutes:02}', ":", f'{seconds:02}')

# Задание 4

proceeds = int(input("Введите сумму выручки:"))
costs = int(input("Введите сумму расходов:"))
if proceeds > costs:
    workers = int(input("Укажите количесство сотрудников:"))
    profit = proceeds-costs
    profitability = round(profit/proceeds, 2)
    workers = round(profit/workers, 2)
    print("Финансовый результат: Прибыль.", "Ее величина:", profit)
    print("Рентабильность выручки составила:", profitability)
    print("Прибыль фирмы в расчете на одного сотрудника составила:", workers)
else:
    profit = proceeds - costs
    print("Финансовый результат: Убыток.", "Его величина:", - profit)
