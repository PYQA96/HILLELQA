"вызов главного метода "
import csv
import datetime
import elasticserch
import humanclass

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
        REGYM = input("Введите режим роботы : ")
        if REGYM != "1" and REGYM != "2":
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
        value = input("Введите значения гендера заново :")
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
    if count_of_nums > 8:
        value = input("Некоректное значение длина меньше чем 8 цыфр, введите заново : ")
        return validate_and_format(value)
    if cleaned_value == "":
        value = input("Некоректное значение пустая строка , введите заново : ")
        return validate_and_format(value)
    else:
        formatted_value = cleaned_value[:2] + '.' + cleaned_value[2:4] + '.' + cleaned_value[4:]
        if int(cleaned_value[4:]) > YEAR:
            value = input("Некоректное значение дата рождения или смерти  не может быть больше чем текущий год : ")
            return validate_and_format(value)
        return formatted_value


def main():
    while True:
        print('-' * 50)
        print("1. Ввести новую запись")
        print("2. Поиск в БД")
        print("3. Экспортировать данные в json формат")
        print("0. Выход")
        print('-' * 50)
        choice = input("Ваш выбор: ")

        if not choice.isdigit() or int(choice) > 5:
            print("Не корректный ввод")
            continue
        elif int(choice) == 0:
            break

        if choice == "1":
            print("Вы будете вводить все данные или только Имя,Дата рождения,пол 1-Сокращенный/2-полный")
            choice = select_work()
            if choice == "1":
                Name = input("введите имя: ")
                Date_of_birth = validate_and_format(input("Дата рождения (в формате день.месяц.год) :"))
                Gander = validate_gender(input("Пол (в фортаме male-Мужчина/female- Женщина) : "))
                human = humanclass.HumanClass(Name, Date_of_birth, Gander,dateofdeath=None)
                choice = select_work()
                if choice == "1":
                    Date_of_death = validate_and_format(input("Дата смерти (в формате день.месяц.год) :"))
                    human.dateofdeath = Date_of_death
                human.human_concatanate()
                print(f"Человек :   {human}")
                print("Человек создан")
            elif choice == "2":
                Name = input("введите имя: ")
                Date_of_birth = validate_and_format(input("Дата рождения (в формате день.месяц.год) :"))
                Gander = validate_gender(input("Пол (в фортаме male-Мужчина/female- Женщина) : "))
                Secondname = input("Отчество : ")
                Thirdname = input("Фамилия : ")
                human = humanclass.HumanClass(Name, Date_of_birth, Gander, secondname=Secondname, thirdname=Thirdname)
                human.human_concatanate()
                print("ОБьект создан")
                print("Жедаете ввести дату смерти ? 1 - Ввод даты смерти, 2 - Отмена")
                choice = select_work()
                if choice == "1":
                        Date_of_death = validate_and_format(input("Дата смерти (в формате день.месяц.год) :"))
                        human.dateofdeath = Date_of_death
                human.human_concatanate()
                print(f"Человек :   {human}")
        elif choice == "2":
            print(f"Введите имя для поиска ")
            Name = input("имя для поиска : ")
            print("*"*50)
            print(*elasticserch.Dependence(Name).Serch())
            print("*" * 50)



    print("Програма закончена")
    print("*" * 60)





if __name__ == "__main__":
    main()
