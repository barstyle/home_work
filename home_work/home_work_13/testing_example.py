# Функция расчета месячного пплатежа по кредиту
# s - сумма займа
# r - годовая процентная ставка от 0 до 1
# n - срок кредита в месяцах
# Пример использования: calculate_credit(20000, 0.12, 36) вернет 664.29
import random


def calculate_credit(s, r, n):
    try:
        data_input = [s, r, n]
        for i in data_input:
            if i >= 0:
                continue
            else:
                return 'Значения не должны быть отрицательными'
        if n > 1200:
            return 'Срок кредита не должен превышать 100 лет'
        elif s == 0:
            return 'Зачем вам 0 деняк в кредит?'
        else:
            r = r / 12
            result = round(float(s * (r * (1 + r) ** n) / ((1 + r) ** n - 1)), 2)
            return result
    except ZeroDivisionError:
        return 'Значения не должны быть равны нулю'
    except OverflowError:
        return 'Небожителям кредиты не нужны'
    except TypeError:
        return 'Значения должны быть числами'


# Простой класс калькулятора
class Calculator():

    # метод сложения чисел
    def sum(self, a, b):
        return a + b

    # метод умножения чисел
    def mult(self, a, b):
        return a * b


if __name__ == '__main__':
    for i in range(1, 100):
        s = random.randint(-10000, 50000)
        print('Loan amount -', s)
        r = float((random.randint(-10, 100))/100)
        print('Percent -', r)
        n = random.randint(1, 1300)
        print('Credit term -', n, '(' + str(int(n/12)), '- years)')
        print('Monthly payment -', calculate_credit(s, r, n))
        print('-'*50)
    print('Monthly payment -', calculate_credit(0.0, 0.12, 36))
    print('Monthly payment -', calculate_credit(100, 0.12, 1202))

    print(Calculator.sum(0, 2, 2))
    print(Calculator.mult(0, 3, 3))
