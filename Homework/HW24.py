class Car():
    FUEL_TYPE = ['бензин', 'дизель', 'электричество', 'гибрид']
    COLORS = []
    NUMBER_OF_CARS = []
    COUNT_OF_CAR = 0


    def __str__(self):
        return f" модель:{self.model} год:{self.year} цвет:{self.color} тип топлива:{self.fuel_type} номер авто:{self.number}"

    @staticmethod
    def is_valid_fuel_type(args):
        if str(args).lower() in Car.FUEL_TYPE:
            return args
        else:
            return Car.FUEL_TYPE[0]


    @property
    def numbers(self):
        return f"{self.number} из {Car.get_number_of_cars() } авто"

    @classmethod
    def get_number_of_cars(cls):
        return len(cls.NUMBER_OF_CARS)


    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    def append_colors(self, color):
        if color not in Car.COLORS:
            Car.COLORS.append(color)
        return color

    def __init__(self, model, year,fuel_type, color,number=""):
        self.model = model
        self.year = year
        self.color = self.append_colors(color)
        self.fuel_type = self.is_valid_fuel_type(fuel_type)
        Car.NUMBER_OF_CARS.append(self)
        Car.COUNT_OF_CAR=Car.COUNT_OF_CAR+1
        self.number=Car.COUNT_OF_CAR


# volvo = Car("model", "year", "color", "дизель")
# volvo1 = Car("model", "year", "color", "дизель")
# a=volvo1.numbers
# print(a)
# print(volvo.__dict__)
# print(volvo1.__dict__)
# print(Car.COLORS)
# print(Car.get_number_of_cars())
# # print(volvo.Count_of_object())
# print(volvo)
car_1 = Car('Zaz', 1979, 'дизель', 'black')
car_2 = Car('BMW', 2000, 'бензин', 'red')
car_3 = Car('VOLVO', 2012, 'электричествоcccc', 'black')
car_4 = Car('Mersedes', 2012, 'гибрид', 'black')
print(Car.COLORS)
print('COLORS:', Car.get_used_colors())  # -> 'COLORS: 2'
print('NUMBER_OF_CARS:', Car.get_number_of_cars())  # -> 'NUMBER_OF_CARS: 4'

for item in (car_1, car_2, car_3, car_4):
 print('item:', item)
 print('numbers:', item.numbers)