# What is the difference between static and class methods?

class Item():
# Static method
    @staticmethod
    def is_integer():
        pass
        '''
        This method (function) should have a relationship with the class. But not something that must be unique per instance.
        Here, we don't pass 'self' as a parameter.
        '''

# Class method
    @classmethod
    def instantiate_from_csv(cls):
        pass
        '''
        This method (function) should have a relationship with the class. These methods are usually used to manipulate
        different structures of data to instantiate objects.
        eg. read data from csv - 100s of objects can be instantiated
        In this, we pass 'cls' as a parameter by default as a class instance.
        '''

# Usually, static or class methods are called at class level instances.

# NOTE: However, those could be also called from instances.

item1 = Item()
item1.is_integer()
item1.instantiate_from_csv()