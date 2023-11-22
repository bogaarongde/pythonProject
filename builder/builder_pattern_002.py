from abc import ABC, abstractmethod

# Define the product class
class Sandwich:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def display(self):
        print("Sandwich with the following ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")


# Define the abstract builder class
class SandwichBuilder(ABC):
    def __init__(self):
        self.sandwich = None

    def create_new_sandwich(self):
        self.sandwich = Sandwich()

    @abstractmethod
    def add_bread(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass

    def get_result(self):
        return self.sandwich


# Define concrete builders
class VeggieSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("Wheat Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Lettuce")
        self.sandwich.add_ingredient("Tomato")
        self.sandwich.add_ingredient("Cucumber")


class HamSandwichBuilder(SandwichBuilder):
    def add_bread(self):
        self.sandwich.add_ingredient("White Bread")

    def add_filling(self):
        self.sandwich.add_ingredient("Ham")
        self.sandwich.add_ingredient("Cheese")
        self.sandwich.add_ingredient("Mayonnaise")


# Define the director class
class SandwichDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_sandwich(self):
        self.builder.create_new_sandwich()
        self.builder.add_bread()
        self.builder.add_filling()
        return self.builder.get_result()


# Client code
veggie_builder = VeggieSandwichBuilder()
director = SandwichDirector(veggie_builder)
veggie_sandwich = director.build_sandwich()

ham_builder = HamSandwichBuilder()
director.builder = ham_builder
ham_sandwich = director.build_sandwich()

# Display sandwiches
print("Veggie Sandwich:")
veggie_sandwich.display()

print("\nHam Sandwich:")
ham_sandwich.display()
