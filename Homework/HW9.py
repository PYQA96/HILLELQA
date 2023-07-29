def infinity_function():
    def descriptor(value):
        result = ""
        value_for_check = value.replace(",", ".").replace("-", "", 1)
        print(value_for_check,"value")
        try:
            number = float(value_for_check)
            result = f"Вы ввели {'положительное' if number > 0 else 'отрицательное' if number < 0 else ''} " \
                     f"{'дробное' if '.' in value_for_check else 'целое'} число: {number}"
        except ValueError:
            result = f"Вы ввели не корректное число: {value}"
        return result
        # value_for_check = value.replace(",", ".", 1)
        # if value_for_check[0] == "-": value_for_check = value_for_check.replace(value[0], "", 1)
        # print(value_for_check)
        # if value_for_check.isdigit():
        #     value = int(value)
        #
        #     if value == 0:
        #         result = f"Вы ввели  {0}"
        #     elif value > 0:
        #         result = f"Вы ввели положительное число {value}"
        #     else:
        #         result = f"Вы ввели отрицательное  число {value}"
        # elif value_for_check.count(".") == 1 and value_for_check.replace(".", "").isdigit() and value_for_check.count(
        #         "-") == 0 and value_for_check[0].isdigit():
        #     value = float(value.replace(",", "."))
        #     if value == 0:
        #         result = f"Вы ввели  {0}"
        #     elif value > 0:
        #         result = f"Вы ввели положительное дробное число {value}"
        #     else:
        #         result = f"Вы ввели отрицательное дробное число {value}"
        # else:
        #     result = f"Вы shit {value}"
        # return result

    while True:
        string_to_input = input()
        if string_to_input.lower() in ["выход", "exit", "quit", "e", "q"]:
            return "Exit with function"
        else:
            answer = descriptor(string_to_input)
            print(answer)
            continue


# 1) целые отрицательные числа, например -5
#
# 2) не верно определяются некоторые не корректные числа и часть из них
# приводит к падению программы, что не желательно. Числа: "5-5", "--56", "3-3.43", "6..6", "..56"
#
# 3) у вас не верно определяются числа с запятой, а не точкой: "-6,7"
#
infinity_function()


print("-" * 50)

# так как я полюбтл рекурсию сделал и вторым вариантом


# def infinity_function1(var):
#     def descriptor(value):
#         result = ""
#         if value.isdigit() and value not in [".", ","]:
#             value = int(value)
#
#             if value == 0:
#                 result = f"Вы ввели  {0}"
#             elif value > 0:
#                 result = f"Вы ввели положительное число {value}"
#             else:
#                 result = f"Вы ввели отрицательное  число {value}"
#         elif value.replace(".", "").replace(",", "").replace("-", "", 1).isdigit() and (
#                 value.count(".") == 1 or value.count(",") == 1):
#             value = float(value)
#             if value == 0:
#                 result = f"Вы ввели  {0}"
#             elif value > 0:
#                 result = f"Вы ввели положительное дробное число {value}"
#             else:
#                 result = f"Вы ввели отрицательное дробное число {value}"
#         else:
#             result = f"Вы shit {value}"
#         return result
#
#     if var.lower() in ["выход", "exit", "quit", "e", "q"]:
#         return print("Exit with function")
#     else:
#         print(descriptor(var))
#         print("Ввод новго числа ")
#         new_data = input()
#         return infinity_function1(new_data)
#
#
# print("Ввод числа")
# var = input()
# print(infinity_function1(var))
