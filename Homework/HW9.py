def infinity_function():
    def descriptor(value):
        result = ""
        if value.isdigit() and value not in [".", ","]:
            value = int(value)

            if value == 0:
                result = f"Вы ввели  {0}"
            elif value > 0:
                result = f"Вы ввели положительное число {value}"
            else:
                result = f"Вы ввели отрицательное  число {value}"
        elif value.replace(".", "").replace(",", "").replace("-", "", 1).isdigit() and value.count(
                ".") == 1 or value.count(",") == 1:
            value = float(value)
            if value == 0:
                result = f"Вы ввели  {0}"
            elif value > 0:
                result = f"Вы ввели положительное дробное число {value}"
            else:
                result = f"Вы ввели отрицательное дробное число {value}"
        else:
            result = f"Вы shit {value}"
        return result

    while True:
        string_to_input = input()
        if string_to_input.lower() in ["выход", "exit", "quit", "e", "q"]:
            return "Exit with function"
        else:
            answer = descriptor(string_to_input)
            print(answer)
            continue


# infinity_function()

print("-" * 50)


# так как я полюбтл рекурсию сделал и вторым вариантом

def infinity_function1(var):

    def descriptor(value):
        result = ""
        if value.isdigit() and value not in [".", ","]:
            value = int(value)

            if value == 0:
                result = f"Вы ввели  {0}"
            elif value > 0:
                result = f"Вы ввели положительное число {value}"
            else:
                result = f"Вы ввели отрицательное  число {value}"
        elif value.replace(".", "").replace(",", "").replace("-", "", 1).isdigit() and (value.count(".") == 1 or value.count(",") == 1):
            value = float(value)
            if value == 0:
                result = f"Вы ввели  {0}"
            elif value > 0:
                result = f"Вы ввели положительное дробное число {value}"
            else:
                result = f"Вы ввели отрицательное дробное число {value}"
        else:
            result = f"Вы shit {value}"
        return result

    if var.lower() in ["выход", "exit", "quit", "e", "q"]:
        return print("Exit with function")
    else:
        print(descriptor(var))
        print("Ввод новго числа ")
        new_data=input()
        return infinity_function1(new_data)

print("Ввод числа")
var = input()
print(infinity_function1(var))