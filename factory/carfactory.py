from abc import ABC, abstractmethod


# Abstract base class for cars
class Car(ABC):
    @abstractmethod
    def assemble(self):
        pass


# Concrete car classes
class Sedan(Car):
    def assemble(self):
        print("Assembling Sedan")


class SUV(Car):
    def assemble(self):
        print("Assembling SUV")


class Truck(Car):
    def assemble(self):
        print("Assembling Truck")


# Car factory
class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "Sedan":
            return Sedan()
        elif car_type == "SUV":
            return SUV()
        elif car_type == "Truck":
            return Truck()
        else:
            raise ValueError("Invalid car type")


# Car order class
class CarOrder:
    def __init__(self, car_type):
        self.car_type = car_type


# Car manufacturer
class CarManufacturer:
    def process_order(self, order):
        car = CarFactory.create_car(order.car_type)
        car.assemble()
        print(f"Delivering {order.car_type}")


# Main function
def main():
    car_manufacturer = CarManufacturer()

    order1 = CarOrder("Sedan")
    order2 = CarOrder("SUV")
    order3 = CarOrder("Truck")

    car_manufacturer.process_order(order1)
    car_manufacturer.process_order(order2)
    car_manufacturer.process_order(order3)


if __name__ == "__main__":
    main()
