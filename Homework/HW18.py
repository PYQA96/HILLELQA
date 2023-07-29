import time

from Homework.HW17 import Auto


class truck(Auto):
    def __init__(self,brand, age,mark,max_load, color="White", weight=None):
        super().__init__(brand, age,mark,color=color, weight=weight)
        self.max_load=max_load
    def move(self):
        print("attention")
        return super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


mits=truck("mits","7","mark","maxload")
print(mits.__dict__)
print(mits.move())



class Car(Auto):
    def __init__(self, brand, age, mark, max_speed , color="White", weight=None):
        super().__init__(brand, age, mark, color=color, weight=weight)
        self.max_speed = max_speed

    def move(self):
        print(super().move())
        return f"max speed is {self.max_speed}"

subaru=Car("subaru","2","car","180")
print(subaru.__dict__)
print(subaru.move())