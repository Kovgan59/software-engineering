class Clock:
    __DAY = 86400   # число секунд в дне
    def __init__(self, sec:int):
        if not isinstance(sec, int):
            raise ValueError("Введено не целое число")

        self.__sec = sec % self.__DAY

    def getFormatTime(self):
        s = self.__sec % 60         # секунды
        m = (self.__sec // 60) % 60 # минуты
        h = self.__sec // 3600 # часы
        return f"{Clock.__getForm(h)}:{Clock.__getForm(m)}:{Clock.__getForm(s)}"

    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0" + str(x)

    def getSeconds(self):
        return self.__sec 

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Необходим тип Clock!")
        return Clock(self.__sec + other.getSeconds())

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Необходим тип Clock!")
        return Clock(self.__sec - other.getSeconds())

c0 = Clock(86400)                  # весь день
c1 = Clock(25200)                  # сон
c2 = Clock(2000)                   # умыться + пожрать
c3 = Clock(3200)                   # дорога до работы
c4 = Clock(29000)                  # работа
c5 = Clock(3200)                   # дорога до дома
c6 = c0 - (c1 + c2 + c3 + c4 + c5) # остается времени до сна

print(f"Времени до начала следующего дня: {c6.getFormatTime()}")   

# c7 = Clock(12.31)
# c7 = c0 + 31
# print(c7)