class Allat:

    def __init__(self, nev):
        self._nev = nev

    def nevetmond(self):
        print(f"A nevem {self._nev}")

class Negylabu:

    LABAK_SZAMA = 4

    def __init__(self):
        print(f"Négylábú vagyok: {self.LABAK_SZAMA}")

class Kutya(Allat):

    FAJ = "Canis"
    def ugat(self):
        print("Vau")

    def nevetmond(self):
        print(f"Én egy kutya vagyok, A nevem {self._nev}, a fajom: {self.FAJ}")

class Macska(Allat, Negylabu):

    FAJ = "Cica"

    def __init__(self,nev,eletkor):
        Allat.__init__(self,nev)
        Negylabu.__init__(self)
        self._eletkor = eletkor
    def nyivak(self):
        print("Miu")

    def nevetmond(self):
        print(f"Én egy macska vagyok, A nevem {self._nev}, a fajom: {self.FAJ} és a korom {self._eletkor} és a lábaim száma {self.LABAK_SZAMA}")



bodri = Kutya("Bodrikutya")

bodri.nevetmond()

bodri.ugat()

cirmi = Macska("Cirmi",3)

cirmi.nevetmond()

cirmi.nyivak()