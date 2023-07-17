import random
# спользовал рекурсию+модуль random

def random_int(number: int):
    print("-"*35)
    print("Введите ваши параметры")
    while True:
            start = input("Введите число начала границы ", )
            stop = input("Введите число конца границы ")
            count_eleents = input("Введите range  ")
            if start.isdigit() == False or  stop.isdigit() == False or count_eleents.isdigit() == False:
                print("дин из ваших параметров не являеться int")
                continue
            else:
                break

    my_array = [random.randint(int(start), int(stop) + 1) for _ in range(int(count_eleents))]
    if number in my_array:
        print(f"Вы угадалои число , оно есть в промежутке , и это {number}")
        result = True
    else:
        print(f"Вы  не угадалои число ,его нет в промежутке  ")
        answer_to_question = input("Желаете продолжить ? ")
        if answer_to_question.lower() in ["y", "д"]:
            print("Введите значение")
            new_int = int(input())
            return random_int(new_int)
        else:
            result = False
    print(f"Вот ваше число  {number} и вот сам массив {my_array}  ")
    print("-" * 35)
    return result, my_array

number=int(input("Введите ваше значение "))
value_to_int, mass_result = random_int(number)

print(f"Для удобства использования распаковал, значение -  {value_to_int} массив - {mass_result}")
