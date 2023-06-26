Name_string = input("Введите произвольную строку: ")

chetniye_chars = Name_string[1::2]


vozvrat_string = Name_string[::-1].upper()

# Вывод результатов
print("Введенная строка:", Name_string)
print("Строка из четных символов:", chetniye_chars)
print("Обратная строка в верхнем регистре:", vozvrat_string)