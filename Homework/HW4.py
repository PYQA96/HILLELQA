stop = True
Name = input("Введите имя ")
while stop:
    Age = input("Введите возраст ")
    Age=int(Age)
    if Age<0 or Age==0 or  not str(Age).isnumeric():
        print("Ошибка, повторите ввод")
    elif 0< Age < 10:
        print(f"Привет, шкет {Name}")
    elif 10<= Age <= 18:
        print(f"Как жизнь {Name}")
    elif 18 < Age < 100 :
        print(f"Что желаете {Name}")
    else:
        print(f"{Name} вы лжете - в наше время столько не живут...")
    Exit = input("Желаете выйти Д\Н: ")
    stop = False if Exit.lower()=="д" else True

