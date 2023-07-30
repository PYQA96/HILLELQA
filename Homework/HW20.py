class String(str):



    def __init__(self,x=""):
        self.x = x

    def __add__(self, other):
        self.x=str(self.x)
        if isinstance(other,list):
            other ="".join(other)
        return String(self.x + str(other))


    def __sub__(self, other):
        ...

