class FoodItem:
    def __init__(self,name,description,price):
        self.name = name
        self.description = description
        self.price = price
    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}"

class Menu:
    def __init__(self):
       self.dishes = []
    def add_dish(self,dish):
        self.dishes.append(dish)
        print(f"\n A dish {dish.name} was added to menu")
    def remove_dish(self,dish):
        self.dishes.remove(dish)
        if dish in self.dishes:
            print(f"\n A dish {dish.name} was removed from menu")
        else:
            print(f"\n A dish {dish.name} wasn't found in menu")

    def __str__(self):
        return '\n'.join([str(dish) for dish in self.dishes])


dish_1 = FoodItem("Borsch" , "A traditional ukrainian dish..." , 150)
dish_2 = FoodItem("Varenyky" , "Boiled dough with various fillings" , 130)
dish_3 = FoodItem("Kulish", "Meat dish on water basis" , 130)
dish_4 = FoodItem("Derynu" , "A dish made of grated potatoes,eggs and flour,which is traditionally fried on a pan" , 75)
menu = Menu()
menu.self_dishes = [dish_1 , dish_2 , dish_3 , dish_4]

menu.remove_dish(dish_3)
menu.add_to_menu(dish_1)

print(menu)

class Order:
    def __init__(self):
        self.order_list = []
    def add_item(self, dish):
        self.order_list.append(dish)
        print(f'\n A dish {dish.name} was added to order')

    def remove_item(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)
            print(f'\n A dish {dish.name} was deleted from order')
        else:
            print(f'\n A dish "{dish.name}" was not found in order)
    def __str__(self):
        bill = 0
        for dish in self.dishes:
            bill += dish.price
        print(f'\n Receipt: {bill} UAH')
        return '\n'.join([str(dish) for dish in self.dishes])

class Restaurant(Order,Menu):
    def __init__(self):
        super().__init__()
        self.menu = Menu()
        self.order = Order()

    def add_food_item(self, dish ):
            self.menu.add_dish(dish)

    def remove_food_item(self, dish):
            self.menu.remove_dish(dish)

    def add_to_order(self, dish):
            self.order.add_item(dish)

    def remove_from_order(self, dish):
            self.order.remove_item(dish)

restaurant = Restaurant()
order = Order()

order.order_list = [dish_4,dish_3, dish_2]
order.remove_item(dish_4)

restaurant.order.add_item(dish_1)

print(order)

with open('receipt.txt', 'w') as file:
    file.write(str(order))

