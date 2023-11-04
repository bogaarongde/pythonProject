class Polygon:
    color = 'piros'
    def __init__(self, sides):
        self.sides = sides
        self.oldalszelesseg = 2


my_polygon = Polygon(4)

my_polygon.color = "valami"

print(my_polygon.color)

print(f"Ennek a polygonnak {my_polygon.sides} oldala van és a színe {my_polygon.color} ")

my_triangle = Polygon(3)

print(f"Ennek a polygonnak {my_triangle.sides} oldala van és a színe {my_triangle.color} ")

Polygon.color = 'kek'
print(f"Ennek a polygonnak {my_triangle.sides} oldala van és a színe {my_triangle.color} ")

print(f"My_polygon polygonnak {my_polygon.sides} oldala van és a színe {my_polygon.color} ")
