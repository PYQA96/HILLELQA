import datetime


class Configs():

    @staticmethod
    def Count_of_year(start, end=None):
        year = int(str(datetime.date.today())[:4])
        if end is None:
            try:
                answer = int(year) - int(start)
            except Exception:
                return "Не указано дату рождения"
        elif end is not None:
            first = start[0]
            second = start[1]
            try:
                answer = str(int(second) - int(first))
            except Exception:
                return "Не указано дату смерти"
        else:
            answer = str(int(year) - int(start))
        if int(answer) < 0:
            return "Не правильно введена да рождения"
        else:
            return answer
