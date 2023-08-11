from humanclass import HumanClass
import config

import humanclass


class Dependence():
    MASSIV = HumanClass.COUNT_OF_HUMAN_DICT

    def __init__(self, search):
        self.search = search

    def __str__(self):
        return f"аргумент для поиска ={self.search} "


    def Serch(self):
        aditional_info = ["male", "female", "Отсутвует дата смерти"]
        result = []

        for human_dict in Dependence.MASSIV:
            found = False
            for value in human_dict.values():
                if value not in aditional_info and str(self.search).lower() in str(value).lower():
                    found = True
                    break

            if found:
                result.append(human_dict)

        return result


