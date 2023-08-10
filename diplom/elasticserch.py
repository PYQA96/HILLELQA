from humanclass import HumanClass
import config

import humanclass


class Dependence():
    MASSIV = HumanClass.COUNT_OF_HUMAN

    def __init__(self, search):
        self.search = search

    def __str__(self):
        return f"аргумент для поиска ={self.search} "

    def Serch(self):
        copy_string_to_equal = []
        aditional_info = ["male", "female", "отсутвует дата смерти"]
        count = 0
        resilt = []
        for key in range(len(Dependence.MASSIV)):
            for value in range(len(Dependence.MASSIV[key])):
                if str(Dependence.MASSIV[key][value]).lower() in aditional_info:
                    continue
                else:
                    for date in range(len(list(Dependence.MASSIV[key][value]))):
                        if str(Dependence.MASSIV[key][value][date]).lower() in list(
                                str(self.search).lower()) and str(
                                Dependence.MASSIV[key][value][date]).lower() not in copy_string_to_equal:
                            count = count + 1
                            copy_string_to_equal.append(str(Dependence.MASSIV[key][value][date]).lower())
                            if count==2:
                                resilt.append(Dependence.MASSIV[key])
                    copy_string_to_equal=[]
                    count = 0
        return resilt


# print(HumanClass.COUNT_OF_HUMAN)
# de = Dependence("ам")
# result = de.Serch()
# print(result)
