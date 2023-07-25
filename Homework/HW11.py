string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
string3 = input("Введите третью строку: ")
string4 = input("Введите четвертую строку: ")


with open("output.txt", "w") as file:
    file.write(string1 + "\n")
    file.write(string2 + "\n")



with open("output.txt", "a") as file:
    file.write(string3 + "\n")
    file.write(string4 + "\n")

file.close()
print("Файл успешно создан и заполнен.")