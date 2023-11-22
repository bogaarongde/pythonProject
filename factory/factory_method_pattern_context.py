import random
from abc import ABC, abstractmethod

# Base abstract class for shapes
class Shape(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, surface):
        pass

# Circle class inheriting from Shape
class Circle(Shape):
    def __init__(self, x, y, radius=20):
        super().__init__(x, y)
        self.radius = radius
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw circle on the given surface
    def draw(self, surface):
        print(f"Drawing a circle at ({self.x}, {self.y}) with radius {self.radius} and color {self.color}")

# Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, x, y, width=50, height=50):
        super().__init__(x, y)
        self.width = width
        self.height = height
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # Draw rectangle on the given surface
    def draw(self, surface):
        print(f"Drawing a rectangle at ({self.x}, {self.y}) with width {self.width}, height {self.height}, and color {self.color}")

# ShapeFactory class for creating shape instances
class ShapeFactory:
    @staticmethod
    def create_shape(context):
        if context.shape_type == "Circle":
            return Circle(context.x, context.y, context.additional_properties.get("radius", 20))
        elif context.shape_type == "Rectangle":
            return Rectangle(
                context.x, context.y,
                context.additional_properties.get("width", 50),
                context.additional_properties.get("height", 50)
            )
        else:
            raise ValueError("Invalid shape type")

# ShapeContext class to hold factory parameters
class ShapeContext:
    def __init__(self, shape_type, x, y, **kwargs):
        self.shape_type = shape_type
        self.x = x
        self.y = y
        self.additional_properties = kwargs

# Main function to create and draw shapes
def main():
    shape_factory = ShapeFactory()
    shapes = []  # List to store created shapes

    # Create random shapes
    for _ in range(5):
        x, y = random.randint(0, 800), random.randint(0, 600)
        shape_type = random.choice(["Circle", "Rectangle"])
        if shape_type == "Circle":
            context = ShapeContext(shape_type, x, y, radius=random.randint(10, 50))
        else:
            context = ShapeContext(shape_type, x, y, width=random.randint(10, 100), height=random.randint(10, 100))
        shape = shape_factory.create_shape(context)
        shapes.append(shape)

    # Draw all the shapes
    for shape in shapes:
        shape.draw(None)  # Itt a Surface paraméter nincs használva, ezért None

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    main()
    print_kwargs(a=1, b=2, c=3)

