class String(str):
    all_objects = []
    def __init__(self, x=""):
        if isinstance(x, list):
            self.x = ",".join(map(str, x))
        elif isinstance(x, int):
            self.x = str(x)
        else:
            self.x = x
        String.all_objects.append(self)

    # применил метод класа для того что бы посмотреть все методы класа
    @classmethod
    def get_all_objects(cls):
        return cls.all_objects

    def __add__(self, other):
        self.x = str(self.x)
        return String(self.x + str(other))

    def __sub__(self, other):
        other=str(other)
        if other in self.x:
            return String(self.x.replace(other,"",1))
        return String(self.x)




#
print(String('New bala7nce') - 7)
print(String(1234) - 5678)
# print(String(['s', ' ', 23]) + ['s', ' ', 23])
# print(String('New') + None)
a2=String(2)
print(a2.__dict__)
a1=String(1234) - 5678
print(a1.__dict__)
#
print(String('New bala7nce') - 7 )                #  ->    'New balance'
print(String('New balance') - 'bal'   )        #  ->    'New ance'
print(String('New balance') - 'Bal'   )        #  ->    'New balance'
print(String('pineapple apple pine') - 'apple') # ->    'pine apple pine'
print(String('New balance') - 'apple'      )    # ->    'New balance'
print(String('NoneType') - None       )        #  ->    'Type'
print(String(55678345672) - 7        )         #  ->    '5568345672'
print(String.all_objects)
a3=String().all_objects
