import json
import csv
import random


with open('data.json', 'r') as file:
    data_dict = json.load(file)

operators = ['095', '066', '098', '096', '050', '097']

for key in data_dict:
    if random.random() < 0.75:  # 75% вероятность, что есть телефон
        phone_number = f"{random.choice(operators)}{''.join(random.choices('0123456789', k=7))}"
        data_dict[key] += (phone_number,)
    else:
        data_dict[key] += ("",)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', 'Имя', 'Возраст', 'Телефон'])
    for key, value in data_dict.items():
        writer.writerow([key, value[0], value[1], value[2]])