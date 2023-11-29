from abc import ABC, abstractmethod
import random

# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass

# Concrete observer class
class Rectangle(Observer):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 0, 0)

    def update(self, subject):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        print(f"Téglalap frissítve: Pozíció: ({self.x}, {self.y}), Szín: {self.color}")

# Subject class
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def move(self, x, y):
        self.x = x
        self.y = y
        self.notify()
        print(f"Kör mozgatva: Pozíció: ({self.x}, {self.y})")

def main():
    # Példányosítjuk a Publisher-t
    circle = Circle(400, 300, 50)

    # Három példány az observer osztályainkból
    rectangles = [
        Rectangle(100, 100, 50, 50),
        Rectangle(200, 200, 50, 50),
        Rectangle(300, 300, 50, 50),
    ]

    # Hozzáadjuk a téglalapokat a körhöz mint megfigyelőket
    for rect in rectangles:
        circle.attach(rect)

    # Teszteljük a rendszert
    circle.move(500, 400)  # Kör mozgatása
    circle.move(600, 500)  # Újabb mozgatás

if __name__ == "__main__":
    main()
