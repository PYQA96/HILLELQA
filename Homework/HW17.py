class Auto:
    def __init__(self, brand, age, mark, color="White", weight=None):
        # представил что цвет белый по умолчанию
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return f"машина {self.brand} едет "

    def stop(self):
        return f"машина {self.brand} едет "

    def birthday(self):
        age_before = self.age
        self.age = int(self.age) + 1
        return f"возраст увеличен на 1 и равен {self.age} лет , до преобразования было  {age_before} лет  "


mazda = Auto("Mazda", "8", "Легковушка")
mazda.name = "Любимое авто"

print(mazda.birthday())
print()
print(mazda.__dict__)


class motocucle(Auto):

    def move(self):
        return f"Мотоцыкл  {self.brand} едет "


kawasaki = motocucle("kawasaki", "7", "Чопер")
kawasaki.name = "Любимый байк"
print(kawasaki.move())
print(kawasaki.__dict__)
