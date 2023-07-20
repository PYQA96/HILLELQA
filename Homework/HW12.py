even_value = lambda x: "Четное" if int(x) % 2 == 0 else "Нечетное"
even_null = lambda x: "Ноль" if int(x) == 0 else even_null(x)

print(even_value(2))
