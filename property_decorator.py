class Auto:
    def __init__(self):
        self._sebesseg = 0

    @property
    def sebesseg(self):
        return self._sebesseg

    @sebesseg.setter
    def sebesseg(self, ertek):
        if ertek >= 0:
            self._sebesseg = ertek
        else:
            print("A sebesség nem lehet negatív!")

my_auto = Auto()

print(my_auto.sebesseg)

my_auto.sebesseg = -3

print(my_auto.sebesseg)