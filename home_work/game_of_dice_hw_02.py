'''
- Программа приветствует игрока в виртуальном казино.
- Игроку предоставляется депозит в 10 000 единиц.
- Программа “бросает кубики” и получает случайное число (используйте модуль random)
  в промежутке от 2 до 12.
- Программа просит пользователя угадать число и сравнивает введенное игроком число с тем,
  которое она загадала. Если пользователь угадал, то ему начисляется 1000 единиц. Если не угадал,
  то от депозита отнимается 1000 единиц.
- Игра продолжается до тех пор, пока у пользователя не кончаются единицы на депозите
  (используйте цикл while).
'''
# Импортируем библиотеку рандом, чтобы ее использовать в будущем
import random

# Приветсвие
print("Приветсвую тебя игрок")

# Заводим переменную в котрой хранится депозит
deposit_user = 10000

print('Ваш депозит равен - ', deposit_user,  'едениц')

count = 0

the_even_log = []

while deposit_user != 0:

    number_casino = random.randint(2, 12)

    number_user = input("\nВведите число от 2 до 12: ")
    if number_user.isdigit() != True:
        while number_user.isdigit() != True:
            number_user = input("\nТы ввел не число\nВведите число от 2 до 12: ")
            if number_user.isdigit() == True:
                continue

    number_user = int(number_user)

    if number_user < 2 or number_user > 12:
        pass
    elif number_casino == int(number_user):
        print('Угадал, выпало число:', number_casino)
        deposit_user = deposit_user + 1000
        print('Ваш депозит равен - ', deposit_user, 'едениц')
    else:
        print("Не Бро, не угадал, выпало число:", number_casino)
        deposit_user = deposit_user - 1000
        print('Ваш депозит равен -', deposit_user,  'едениц')

    count = count + 1
    print('Попытка -', count)

    log = []
    log.append(number_casino)
    log.append(count)
    log.append(deposit_user)
    print(log)

    the_even_log.append(log)

print(the_even_log)
