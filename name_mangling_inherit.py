class AlapOsztaly:
    def __init__(self):
        self.__privat_attributum = "AlapOsztaly privat attribútuma"

    def kiir(self):
        print(f"AlapOsztaly: {self.__privat_attributum}")


class Leszarmazott(AlapOsztaly):
    def __init__(self):
        super().__init__()
        self.__privat_attributum = "Leszarmazott privat attribútuma"

    def kiir(self):
        print(f"Leszarmazott: {self.__privat_attributum}")
        super().kiir()


# Tesztelés
obj = Leszarmazott()
obj.kiir()

# Output:
# Leszarmazott: Leszarmazott privat attribútuma
# AlapOsztaly: AlapOsztaly privat attribútuma
