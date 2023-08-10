import datetime
class Configs():

    @staticmethod
    def Count_of_year(start,end=None):
        year = int(str(datetime.date.today())[:4])
        if end is None:
            try:
                return str(year-start)
            except Exception:
                return "Не указано дату рождения"
        elif end is not  None :
            end=start[1]
            start=start[0]
            try:
                return str(end - start)
            except Exception:
                return "Не указано дату смерти"
        else:return str(year-start)





