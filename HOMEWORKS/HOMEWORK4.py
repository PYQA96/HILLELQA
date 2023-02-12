import math

from unicodedata import decimal


# Завдання 1.
#
# Написати функцію, яка буде переводити градуси в радіани (без використання math.radians).
# Використовуючи цю функцію, вивести на екран значення косинусів кутів 60, 45 та 40 градусів.
#
# 	def degrees2radians(degrees): # returns float: radians value
#             pass
def degrees2radians(degrees):  # returns float: radians value
    return round((180 / math.pi) * degrees, 4)


degrees2radians(1)
print(degrees2radians(1))


# Завдання 2.
#
# Користувач вводить довжини катетів прямокутного трикутника. Написати функцію,
# яка обчислить площу та периметр цього трикутника. Функція має повертати пару значень.
#
def triangle_square_and_perimeter(a, b):  # returns 2 values
    c = math.sqrt(a ** 2 + b ** 2)
    S = round(((a * b) / 2), 2)
    P = round((a + b + c), 2)
    return S, P


answer1, answer2 = triangle_square_and_perimeter(2, 5)
print(answer1, answer2)


#
#
# Завдання 3.
#
# Написати функцію, яка обчислює площу та об'єм конуса за його радіусом та висотою. Функція має повертати два значення.
#
def cone_square_and_volume(radius, height):  # returns 2 floats
    v = math.pi * radius * radius * height / 3
    s = math.pi * radius * math.sqrt(radius ** 2 + height ** 2)
    v, s = round(v, 2), round(s, 2)
    return v, s


answer1, answer2 = cone_square_and_volume(2, 3)
print(cone_square_and_volume(2, 3))
print(answer1, answer2)


#
# Завдання 4.
#
# Написати функцію, що приймає безкінечну кількість чисел позиційними параметрами та іменований параметр
# start зі значенням за замовчуванням 0. Функція має повертати суму усіх переданих параметрами чисел та числа start.
# Функція повинна називатися my_sum. Для розрахунку суми використайте вбудовану функцію sum.

def my_sum( start=0,*vars ):
    nums=sum([i for i in vars])
    return nums



print(my_sum(1, 2, 3))
