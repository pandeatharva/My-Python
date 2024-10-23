# Store Management System Project

import csv


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

    @classmethod    #decorator - to convert this method into class method
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count the floats that are point zero decimal  eg. 4.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def calculate_total_price(self):
        return self.price * self.quantity


# item1 = Item("Phone", 100, 3)
# # item1.name = "Phone"
# # item1.price = 100
# # item1.quantity = 5
# print(item1.calculate_total_price())
#
# item2 = Item("Laptop", 800, 7)
# print(item2.calculate_total_price())
#
# item3 = Item("Cable", 10, 10)
# item4 = Item("Mouse", 25, 5)
# item5 = Item("Keyboard", 50, 4)

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


# for item in Item.all:
#     print(item.name)


# Item.instantiate_from_csv()
# print(Item.all)

################# Inheritance

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity: int, broken_phones):
    # Call super function to access to all attributes from Parent class
        super().__init__(
            name, price, quantity
        )

    # Run validations to the received arguments
    assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than 0"

    # Assign to self objects
    self.broken_phones = broken_phones

    #Action to execute
    Phone.all.append(self)

phone1 = Phone("iPhonev10", 600, 3,1)

print(Item.all)
print(Phone.all)
