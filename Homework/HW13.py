import random

my_array = [random.randint(int(1), int(10)) for _ in range(int(5))]
print(my_array)
def summ_masiv(value: list):
    dictionary = {item: value.count(item) for item in value}
    print(dictionary)
    end_of_vivod = lambda x: str(x) + " Разa" if int(x) in [2,3,4]  else str(x) + " Раз"
    result_dictionary={}
    for key, value in dictionary.items():
        print(key, value)
        result_dictionary[key] = end_of_vivod(value)
    return dict(sorted(result_dictionary.items()))


print(summ_masiv(my_array))
