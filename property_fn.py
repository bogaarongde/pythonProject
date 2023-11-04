class Auto:
    def __init__(self):
        self._sebesseg = 0

    def get_sebesseg(self):
        print("Ez a getter")
        return self._sebesseg

    def set_sebesseg(self, ertek):
        if ertek >= 0:
            self._sebesseg = ertek
        else:
            print("A sebesség nem lehet negatív!")

    sebessegek = property(get_sebesseg, set_sebesseg)


my_auto = Auto()

print(my_auto.sebessegek)

my_auto.sebessegek = -3

print(my_auto.sebessegek)
