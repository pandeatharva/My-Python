# Store Management System Project

class Item:
    pay_rate = 0.8 # Class attribute  # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        #print(f"I am created!: {name}, {price}, {quantity}")

        # Run validations to the received arguments
        assert price >= 0, f"price {price} is not greater than 0"
        assert quantity >= 0, f"quantity {quantity} is not greater than 0"

        # Assign to self objects
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 3)
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5
print(item1.calculate_total_price())

item2 = Item("Laptop", 800, 7)
# item2.name = "Laptop"
# item2.price = 500
# item2.quantity = 3
print(item2.calculate_total_price())

item3 = Item("Cable", 10, 10)
item4 = Item("Mouse", 25, 5)
item5 = Item("Keyboard", 50, 4)

# item1.apply_discount()
# print(item1.price)
#
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

print(Item.all)

for item in Item.all:
    print(item.name)