class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product = Product(10)
print(product.price())

# It is not always compulsory to have both setter and getter methods. If the setter method is deleted, 
#then it is not possible to change the value again
# Above we a have used decorators of property instead of creating a separate property and two different
#functions of set_value and get_value.

# Refer the video for more detailed explanation 