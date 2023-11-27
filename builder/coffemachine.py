# Builder Design Pattern for Coffee Machine

# Product class
class CoffeeMachine:
    def __init__(self):
        self.water_tank_size = None
        self.coffee_bean_container_size = None

    def describe(self):
        print(f"Coffee Machine with {self.water_tank_size}L water tank and {self.coffee_bean_container_size}g coffee bean container.")

# Builder abstract class
class CoffeeMachineBuilder:
    def __init__(self):
        self.coffee_machine = CoffeeMachine()

    def set_water_tank_size(self, size):
        self.coffee_machine.water_tank_size = size

    def set_coffee_bean_container_size(self, size):
        self.coffee_machine.coffee_bean_container_size = size

    def get_coffee_machine(self):
        return self.coffee_machine

# Concrete builder classes
class SmallCoffeeMachineBuilder(CoffeeMachineBuilder):
    def build(self):
        self.set_water_tank_size(1.0)
        self.set_coffee_bean_container_size(200)
        return self.get_coffee_machine()

class LargeCoffeeMachineBuilder(CoffeeMachineBuilder):
    def build(self):
        self.set_water_tank_size(2.0)
        self.set_coffee_bean_container_size(500)
        return self.get_coffee_machine()

# Director class
class CoffeeMachineDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        return self.builder.build()

# Client code
small_builder = SmallCoffeeMachineBuilder()
large_builder = LargeCoffeeMachineBuilder()

director = CoffeeMachineDirector(small_builder)
small_coffee_machine = director.construct()
small_coffee_machine2 = director.construct()


director = CoffeeMachineDirector(large_builder)
large_coffee_machine = director.construct()

small_coffee_machine.describe()
small_coffee_machine2.describe()
large_coffee_machine.describe()
