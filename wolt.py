
class Food:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:

    def __init__(self, menu_items: list[Food], name: str):  # type hinting
        self.menu_items = menu_items
        self.name = name

    def __str__(self):
        return f"Ez egy resturant osztály, az étterem neve {self.name}"

    def __add__(self, other):
        if not isinstance(other, Food):
            raise TypeError("Egy ételt adj hozzá")
        else:
            self.menu_items.append(other)

    def getmenuitems(self):
        for menu_item in self.menu_items:
            print(f"{menu_item.name}{'.' * (20 - len(menu_item.name) - len(str(menu_item.price)))}{menu_item.price} Ft")


my_menu = [Food('Hambi', 100), Food('Krumpli', 100)]

my_restaurant = Restaurant(my_menu, "Kifli étterem")

print(my_restaurant)

my_restaurant + Food('Béka', 210)

my_restaurant.getmenuitems()


for i in range(2):
    input_name = input("Add meg, hogy melyik elemet szeretnéd: ")
    input_price = input("Add meg, hogy mennyiért: ")
    my_restaurant + Food(input_name, input_price)


my_restaurant.getmenuitems()
