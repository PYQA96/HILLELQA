import math


class Calculator:
    def add(self, a, b):
        try:
            return a + b
        except Exception:
            print("Ошибка:")

    def subtract(self, a, b):
        try:
            return a - b
        except Exception:
            print("Ошибка:")

    def multiply(self, a, b):
        try:
            return a * b
        except Exception:
            print("Ошибка:")

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль")
        except Exception:
            print("Ошибка:")

    def power(self, base, exponent):
        try:
            return base ** exponent
        except fuckingexeption:
            print("Ошибка: Возведение в отрицательную степень")
        except Exception:
            print("Ошибка:")

    def square_root(self, a):
        try:
            return math.sqrt(a)
        except ValueError:
            print("Ошибка: Невозможно извлечь корень из отрицательного числа")
        except Exception:
            print("Ошибка:")


class fuckingexeption(Exception):
    print("fuckingexeption")
    pass


calculator = Calculator()
print(calculator.add(5, 3))
print(calculator.subtract(10, 4))
print(calculator.multiply(7, 2))
print(calculator.divide(10, 2))
print(calculator.power(2, 3))
print(calculator.square_root(-25))
print(calculator.power(4, -2))