class Observer:
    def update(self, temperature):
        pass

class Hírügynökség(Observer):
    def update(self, temperature):
        print(f"Hírügynökség: Az aktuális hőmérséklet {temperature}°C.")

class IdőjárásJelentés(Observer):

    def __init__(self):
        self.infoszam = 0
        self.atlaghomerseklet = 0

    def update(self, temperature):
        if self.infoszam != 0:
            self.atlaghomerseklet = (self.atlaghomerseklet*self.infoszam + temperature)/(self.infoszam + 1)
        else:
            self.atlaghomerseklet = temperature
        self.infoszam+=1

        print(f"IdőjárásJelentés: Az átlag hőmérséklet: {self.atlaghomerseklet}°C.")

class HőmérsékletMérő:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def attach(self, observer):
        self.observers.append(observer)

    def setHőmérséklet(self, temperature):
        self.temperature = temperature
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)

def main():
    thermometer = HőmérsékletMérő()
    hirugynokseg = Hírügynökség()
    idojarasjelentes = IdőjárásJelentés()

    thermometer.attach(hirugynokseg)
    thermometer.attach(idojarasjelentes)

    thermometer.setHőmérséklet(23)
    thermometer.setHőmérséklet(32)
    thermometer.setHőmérséklet(5)

if __name__ == "__main__":
    main()
