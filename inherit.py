class Allat:
    def __init__(self, nev):
        self.nev = nev

    def hangot_ad(self):
        pass

    def mi_a_neved(self):
        print(self.nev)

class Negylabu:
    LABAK_SZAMA = 4

    def __init__(self):
        print('negylabu')
class Macska(Allat,Negylabu):
    def __init__(self, nev, eletkor):
        Allat.__init__(self,nev)
        Negylabu.__init__(self)
        self.eletkor = eletkor

class Kutya(Allat):
    def hangot_ad(self):
        print("Vau")


tom = Macska('Tom',7)

bodri = Kutya('Bodri')

bodri.hangot_ad()
bodri.mi_a_neved()
print(tom.LABAK_SZAMA)


