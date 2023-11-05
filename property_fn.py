class Auto:
    def __init__(self):
        self._sebesseg = 0

    def get_sebesseg(self):
        print("Ez a getter")
        return self._sebesseg

    def set_sebesseg(self, ertek):
        print("Ez a setter")
        if ertek >= 0:
            self._sebesseg = ertek
        else:
            print("A sebesség nem lehet negatív!")

    sebesseg = property(get_sebesseg, set_sebesseg)


my_auto = Auto()

print(my_auto.sebesseg)

my_auto.sebesseg = -3

print(my_auto.sebesseg)
