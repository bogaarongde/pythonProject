class Auto:

    def __init__(self):
        self._sebesseg = 0

    @property
    def sebesseg(self):
        print("Ez a getter")
        return self._sebesseg

    @sebesseg.setter
    def sebesseg(self,ujsebesseg):
        print("Ez a setter")
        self._sebesseg = ujsebesseg


my_auto = Auto()

my_auto.sebesseg = 120

print(my_auto.sebesseg)