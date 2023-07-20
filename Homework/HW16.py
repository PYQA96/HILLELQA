from datetime import datetime

def simple_function(func):
    print("Моя первая функция")
    def timex():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f"Время выполнения функции: {execution_time}")
        print("Конец функкции ")
    return timex


@simple_function
def strong_function():
    mass=[i for i in range(1000000) if i%2==0]
    print("Моя вторая функция")

strong_function()


