class myMath:
    def __init__(self):
        pass

    def osszead(self,a,b):
        c = self._resz_osszead(a, b)
        return c

    def _resz_osszead(self, a, b):
        return a + b


my_math = myMath()

print(my_math.osszead(4,5))

szam1 = int(input("írj be egy számot "))

if not isinstance(szam1, int):
    raise TypeError("Nem szám")


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

