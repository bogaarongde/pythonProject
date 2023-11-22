import random
from abc import ABC, abstractmethod

# Base abstract class for shapes
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = random.randint(10, 50)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw circle
    def draw(self):
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius} and color {self.color}")

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw rectangle
    def draw(self):
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width}, height {self.height}, and color {self.color}")

# ShapeFactory class for creating shape instances
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, x, y):
        if shape_type == "Circle":
            return Circle(x, y)
        elif shape_type == "Rectangle":
            return Rectangle(x, y)
        else:
            raise ValueError("Invalid shape type")

# Main function to create and draw shapes
def main():
    shape_factory = ShapeFactory()
    shapes = []  # List to store created shapes

    # Create random shapes
    for _ in range(5):
        x, y = random.randint(0, 800), random.randint(0, 600)
        shape_type = random.choice(["Circle", "Rectangle"])
        shape = shape_factory.create_shape(shape_type, x, y)
        shapes.append(shape)

    # Draw all the shapes
    for shape in shapes:
        shape.draw()

if __name__ == "__main__":
    main()
