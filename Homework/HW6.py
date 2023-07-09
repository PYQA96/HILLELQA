chess_players = {
    "Carlsen, Magnus": 1865,
    "Firouzja, Alireza": 2804,
    "Ding, Liren": 2799,
    "Caruana, Fabiano": 1792,
    "Nepomniachtchi, Ian": 2773
}
result = []
chess_players_names = {values: keys for keys, values in chess_players.items()}
print(chess_players_names)
for age, name in chess_players_names.items():
    second = []
    if age > 2000:
        name = name.split(" ")
        name[1] = name[1][:1]
        name = " ".join(name)
        second.append(age)
        second.append(name)
        result.append(tuple(second))
print(result)
res = {key: value for key, value in result}
print(res)
