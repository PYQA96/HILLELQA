import config


class HumanClass():
    COUNT_OF_HUMAN_DICT = []

    def __str__(self):
        return f"Имя: {self.name} | Дата рождения: { 'Отсутвует' if self.dateofbirth == None else self.dateofbirth} " \
               f"| Гендер: { 'Отсутвует' if self.gender == None else self.gender} | Второе имя: {'Отсутвует' if self.secondname == None else self.secondname}" \
               f"| Фамилия:  {'Отсутвует' if self.thirdname == None else self.thirdname} | Дата смерти: {'Отсутвует' if self.dateofdeath == None else self.dateofdeath} "

    def __init__(self, name, dateofbirth, gender, secondname=None, thirdname=None, dateofdeath=None):
        self.name = name
        self.dateofbirth = dateofbirth
        self.gender = gender
        self.secondname = secondname
        self.thirdname = thirdname
        self.dateofdeath = dateofdeath

    "форматирую дату , после чего использую в  def human_concatanate(self):"

    def formate_dtae(self, dateofbirth, dateofdeath=None):
        mass = [" ", ".", ",", "--", "_", "  ", "   ", "/", "'\'"]
        try:
            dateofbirth = list(dateofbirth)
            for value in range(len(dateofbirth)):
                if dateofbirth[value] in mass or str(dateofbirth[value]).isalpha():
                    dateofbirth[value] = "-"
            dateofbirth = "".join(dateofbirth)
            dateofbirth = str(dateofbirth).split("-")
            if dateofdeath is not None:
                dateofdeath = list(dateofdeath)
                for value in range(len(dateofdeath)):
                    if dateofdeath[value] in mass or str(dateofdeath[value]).isalpha():
                        dateofdeath[
                            value] = "-"
                dateofdeath = "".join(dateofdeath)
                dateofdeath = str(dateofdeath).split("-")
                return int(max(dateofbirth, key=int)), int(max(dateofdeath, key=int))
            return int(max(dateofbirth, key=int))
        except ValueError:
            return int(max(dateofbirth, key=int))

    "Добавленияе масива из атрибутов  обьекта класа  в общий массив класа COUNT_OF_HUMAN"

    def human_concatanate(self):
        answer_template = ""
        seconddate, firstdate = "Отсутвует дата смерти", self.dateofbirth
        if self.dateofdeath is not None or str(self.dateofdeath).isdigit():
            seconddate = self.dateofdeath
            firstdate = self.dateofbirth
        if self.dateofdeath is None or self.dateofdeath is not type(str):
            answer_template = self.formate_dtae(self.dateofbirth, self.dateofdeath)
        else:
            self.dateofbirth, self.dateofdeath = self.formate_dtae(self.dateofbirth, self.dateofdeath)
        if self.secondname is None and self.thirdname is None:
            return HumanClass.COUNT_OF_HUMAN_DICT.append({
                "имя": self.name,
                "дата рождения": firstdate,
                "дата смерти": seconddate,
                "полл": self.gender,
                "возраст": config.Configs.Count_of_year(answer_template, self.dateofdeath)
            })
        elif self.secondname is None and self.thirdname is not None:
            return HumanClass.COUNT_OF_HUMAN_DICT.append({
                "имя": self.name,
                "дата рождения": firstdate,
                "дата смерти:": seconddate,
                "полл": self.gender,
                "Фамилия": self.thirdname,
                "возрас": config.Configs.Count_of_year(answer_template, self.dateofdeath)
            })
        elif self.secondname is not None and self.thirdname is None:
            return HumanClass.COUNT_OF_HUMAN_DICT.append({
                "имя": self.name,
                "дата рождения": firstdate,
                "дата смерти:": seconddate,
                "полл": self.gender,
                "отчество": self.secondname,
                "возраст": config.Configs.Count_of_year(answer_template, self.dateofdeath)
            })
        else:
            return HumanClass.COUNT_OF_HUMAN_DICT.append({
                "имя": self.name,
                "дата рождения": firstdate,
                "дата смерти:": seconddate,
                "полл": self.gender,
                "Фамилия": self.thirdname,
                "отчество": self.secondname,
                "возраст": config.Configs.Count_of_year(self.dateofbirth, self.dateofdeath)
            })
