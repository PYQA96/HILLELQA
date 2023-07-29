import json

# Создание словаря
data_dict = {
    123456: ('Иван', 25),
    987654: ('Анна', 30),
    456789: ('Петр', 22),
    654321: ('Мария', 28),
    789456: ('Ольга', 35)
}

# Запись словаря в json-файл
with open('data.json', 'w',"utf-8") as file:
    json.dump(data_dict, file)

print("Словарь успешно сохранен в файл data.json")