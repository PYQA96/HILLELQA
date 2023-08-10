"вызов главного метода "
import csv
import datetime
import elasticserch
import humanclass
import config

REGYM = ""
ANSWER = ""
YEAR = int(str(datetime.date.today())[:4])


class CsvExporter:
    def __init__(self, filename):
        self.filename = filename

    def export_data(self, data):
        with open(self.filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Name", "Date of Birth", "Gender", "Second Name", "Third Name", "Date of Death"])
            for row in data:
                csv_writer.writerow(row)


def select_work():
    try:
        REGYM = int(input("Введите режим роботы : "))
        if REGYM != 1 and REGYM != 2:
            print("Числа не входят в перечень ")
            return select_work()
        return REGYM
    except ValueError:
        print("Ошибка при вводе, введите число ")
        print("_" * 50)
        return select_work()


def validate_gender(value):
    value = str(value).lower()
    if value == "male":
        return value
    elif value == "female":
        return value
    else:
        print("Введите значения гендера заново")
        value = input()
        return validate_gender(value)


def validate_and_format(value):
    value = list(value)
    cleaned_value = ""
    count_of_nums = 0
    if len(value) > 10:
        value = input("Некоректное значение, введите заново,  длина больше чем 8 цыфр: ")
        return validate_and_format(value)
    for i in range(len(value)):
        if str(value[i]).isdigit():
            cleaned_value += value[i]
            count_of_nums = count_of_nums + 1
    if count_of_nums <= 6:
        value = input("Некоректное значение длина меньше чем 8 цыфр, введите заново : ")
        return validate_and_format(value)
    if cleaned_value == "":
        value = input("Некоректное значение пустая строка , введите заново : ")
        return validate_and_format(value)
    else:
        formatted_value = cleaned_value[:2] + '.' + cleaned_value[2:4] + '.' + cleaned_value[4:]
        if int(cleaned_value[4:]) > YEAR:
            value = input("Некоректное значение дата рождения не может быть больше чем текущий год : ")
            return validate_and_format(value)
        return formatted_value


while True:
    Name = None
    Date_of_birth = None
    Gander = None
    Secondname = None
    Thirdname = None
    Date_of_death = None
    print("Здравствуйте, выберите что вы хотите сделать")
    print("Режимы роботы:  цыфра 1 - добавление человека,  цыфра 2 - поиск человека")
    ANSWER = select_work()
    if ANSWER == 1:
        print("Необходимо ввечти 3 параметра обязательных Имя,Дата рождения,Пол - каждое с новой строки")
        Name = input("введите имя: ")
        Date_of_birth = validate_and_format(input("Дата рождения (в формате день.месяц.год) :"))
        Gander = validate_gender(input("Пол (в фортаме male-Мужчина/female- Женщина) : "))
        print(f"Ок, вы ввели имя:-{Name} | Дата рождения:-{Date_of_birth} | Пол:-{Gander}")
        print("Так же можете ввести Фамилию и отчесто - 1 - Ввод отчества и Фамилии, 2 - Отмена")
        input_answ = select_work()
        if input_answ == 1:
            Secondname = input("Отчество : ")
            Thirdname = input("Фамилия : ")
            print("Жедаете ввести дату смерти ? 1 - Ввод даты смерти, 2 - Отмена")
            Date_of_death = validate_and_format(
                input("дата смерти (в формате день.месяц.год) : ")) if select_work() == 1 else None
            human = humanclass.HumanClass(Name, Date_of_birth, Gander, secondname=Secondname, thirdname=Thirdname,
                                          dateofdeath=Date_of_death)
            print(f"Человек :   {human}")
            human.human_concatanate()
            print("Обьект добавлен в архив")
        else:
            print("Жедаете ввести дату смерти ? 1 - Ввод даты смерти, 2 - Отмена")
            Date_of_death = validate_and_format(
                input("дата смерти  (в формате день.месяц.год) : ")) if select_work() == 1 else None
            human = humanclass.HumanClass(Name, Date_of_birth, Gander, dateofdeath=Date_of_death)
            human.human_concatanate()
            print(f"Поздравляю вы ввели  {human}")
    else:
        print(f"Введите имя для поиска ")
        Name = input("имя для поиска : ")
        name_for_serch = elasticserch.Dependence(Name)
        print(f"Вы ввели имя для поиска {name_for_serch}")
        answer = name_for_serch.Serch()
        print(answer)
        print(f"Желаете загрузить данные ?")
        data = name_for_serch.Serch()
        csv_exporter = CsvExporter("output.csv")
        csv_exporter.export_data(data)
        print("Данные автоматически загружены")
    print("Завершить роботу 1 - Продолжить роботу с архивом, 2 -завершить роботу")

    answer = select_work()
    if answer == 1:
        continue
    else:
        break
