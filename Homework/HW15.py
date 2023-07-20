def is_polindrom(value : list):
   result_masiv=list(filter(lambda x: True if x[::-1]==x[::] else False,value))
   return result_masiv



inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']
print(is_polindrom(inputdata))



# Ламбда функции великолепны