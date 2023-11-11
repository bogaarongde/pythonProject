from abc import ABC,abstractmethod
class AbstractSzamla(ABC):
    @abstractmethod
    def kiir_egyenleg(self):
        pass

class BankSzamla(AbstractSzamla):
    pass

    def kiir_egyenleg(self):
        print("bankszamla")

mybankszamla = BankSzamla()

mybankszamla.kiir_egyenleg()

