# Name: Marco Arnoldi
# Date: 2023/11/02
# Description:
# This program is a burger shop that allows the user to order a burger, side, drink, or combo.

class FoodItem:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories
    def __str__(self):
        return f"({self.name} - ${self.price} - {self.calories} calories)"
        
class Burger(FoodItem):
    def __init__(self, name, price, calories, patty_type, toppings):
        super().__init__(name, price, calories)
        self.patty_type = patty_type
        self.toppings = toppings

    def __str__(self):
        toppings_str = ", ".join(self.toppings) if self.toppings else "None"
        return (
            f"{self.name} - ${self.price:.2f} - {self.calories} calories\n"
            f"Patty: {self.patty_type}\nToppings: {toppings_str}"
        )

        
class Drink(FoodItem):
    def __init__(self, name, price, calories, size):
        super().__init__(name, price, calories)
        self.size = size
    def __str__(self):
        return f"({self.name} - ${self.price} - {self.calories} calories)\nSize: {self.size}"

class Side(FoodItem):
    def __init__(self, name, price, calories, side_type):
        super().__init__(name, price, calories)
        self.side_type = side_type
    def __str__(self):
        return f"({self.name} - ${self.price} - {self.calories} calories)\nSide: {self.side_type}"
        
class Combo(FoodItem):
    def __init__(self, name, price, calories, burger, drink, side):
        super().__init__(name, price, calories)
        self.burger = burger
        self.drink = drink
        self.side = side

    def __str__(self):
        return (
            f"{self.name} - ${self.price:.2f} - {self.calories} calories\n"
            f"Burger: {self.burger}\nDrink: {self.drink}\nSide: {self.side}"
        )

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    def total_calories(self):
        total = 0
        for item in self.items:
            total += item.calories
        return total
    def item_names(self):
        names = []
        for item in self.items:
            if isinstance(item, Burger):
                names.append(f"Burger: {item.patty_type} with {', '.join(item.toppings)}")
            elif isinstance(item, Drink):
                names.append(f"Drink: {item.name} - {item.size}")
            elif isinstance(item, Side):
                names.append(f"Side: {item.name}")
            elif isinstance(item, Combo):
                names.append(f"Combo: {item.name} ({item.burger.patty_type}, {item.drink.name}, {item.side.name})")
        return names

    def __str__(self):
        return f"\nCustomer: {self.customer_name}\nItems: {self.item_names()}\nTotal calories: {self.total_calories()}\nTotal: ${self.total_price()}\n"

def user_input_burger():
    print("Which type of patty would you like?")
    print("1. Beef\n2. Chicken\n3. Veggie\n4. Cancel")
    patty_type = input("Please enter your selection: ")
    if patty_type == "1":
        patty_type = "beef"
    elif patty_type == "2":
        patty_type = "chicken"
    elif patty_type == "3":
        patty_type = "veggie"
    elif patty_type == "4":
        return None  # Return None when the user cancels
    else:
        print("Please enter a valid selection.")
        return None
        
    print("Which toppings would you like?")
    print("1. Cheese\n2. Lettuce\n3. Tomato\n4. Onion\n5. Pickles\n6. Done")
    toppings_list = []
    
    while len(toppings_list) < 3:
        toppings = input("Please select up to 3 toppings: ")   
        if toppings == "1":
            toppings_list.append("cheese")
        elif toppings == "2":
            toppings_list.append("lettuce")
        elif toppings == "3":
            toppings_list.append("tomato")
        elif toppings == "4":
            toppings_list.append("onion")
        elif toppings == "5":
            toppings_list.append("pickles")
        elif toppings == "6":
            break
        else:
            print("Please enter a valid selection.")
            return None
    
    b = Burger("McBurger", 5.99, 500, patty_type, toppings_list)
    return b


def user_input_drink():
    print("Which drink would you like?")
    print("1. Soda\n2. Juice\n3. Water")
    
    drink_type = input("Please enter your selection: ")
    if drink_type == "1":
        drink_type = "soda"
    elif drink_type == "2":
        drink_type = "juice"
    elif drink_type == "3":
        drink_type = "water"
    elif drink_type == "4":
        return None
    else:
        print("Please enter a valid selection.")
        return
    
    print("What size would you like?")
    print("1. Small\n2. Medium\n3. Large\n 4. Cancel")
    
    drink_size = input("Please enter your selection: ")
    calories = 0
    price = 0.0
    if drink_size == "1":
        drink_size = "small"
        calories = 100
        price = 1.99
    elif drink_size == "2":
        drink_size = "medium"
        calories = 150
        price = 2.49
    elif drink_size == "3":
        drink_size = "large"
        calories = 200
        price = 2.99
    elif drink_size == "4":
        return None
    else:
        print("Please enter a valid selection.")
        return
        
    d = Drink(f"{drink_type} McDrink", price, calories, drink_size)
    return d

def user_input_side():
    print("Which side would you like?")
    print("1. Fries\n2. Onion Rings\n3. Salad\n 4. Cancel")
    
    side_type = input("Please enter your selection: ")
    if side_type == "1":
        side_type = "fries"
        calories = 200
    elif side_type == "2":
        side_type = "onion rings"
        calories = 170
    elif side_type == "3":
        side_type = "salad"
        calories = 80
    elif side_type == "4":
        return None
    else:
        print("Please enter a valid selection.")
        return        
        
    s = Side(f"{side_type} McSide", 1.99, calories, side_type)
    return s

def user_input_combo():
    print("Which combo would you like?")
    print("1. Small\n2. Medium\n3. Large\n 4. Cancel")
    
    combo_size = input("Please enter your selection: ")
    if combo_size == "1":
        combo_size = "small"
        price = 5.99
    elif combo_size == "2":
        combo_size = "medium"
        price = 6.99
    elif combo_size == "3":
        combo_size = "large"
        price = 7.99
    elif combo_size == "4":
        return None
    else:
        print("Please enter a valid selection.")
        return
        
    b = user_input_burger()
    d = user_input_drink()
    s = user_input_side()
    c = Combo(f"{combo_size} McCombo", price, 0, b, d, s)
    return c
    
def take_order():
    name = input("What is your name?: ")   
    if name == "":
        name = "Guest"
    order = Order(name)
    
    while True:
        #ask the user for what they would like to order
        print("What would you like to order?")
        print("1. Burger\n2. Side\n3. Drink\n4. Combo")
        food_order = input("Please enter your selection: ")
        if food_order == "1":
            b = user_input_burger()
            print(b)
            if b is not None:
                order.add_item(b)
        elif food_order == "2":
            s = user_input_side()
            if s is not None:
                order.add_item(s)
        elif food_order == "3":
            d = user_input_drink()
            if d is not None:
                order.add_item(d)
        elif food_order == "4":
            c = user_input_combo()
            if c is not None:
                order.add_item(c)
        else:
            print("Sorry, we don't have that.")
        #ask the user if they would like to order anything else
        order_again = input("Would you like to order anything else? (y/n): ")
        if order_again == "n":
            break
    
    print("Thank you for your order!")
    print("Order details: " + str(order))

print("Welcome to Burger Shop")
take_order()


    