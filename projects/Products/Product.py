class Product:
    def __init__(self, product_id, name, price):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
# Encapsulation used here
    @property
    def product_id(self):
        return self.__product_id
    
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price













# class Product:
#     """
#     Represents a product with immutable properties.
#     Properties: product_id, name, price.
#     """
#     def __init__(self, product_id, name, price):
#         # Use private attributes (conventionally starting with _)
#         self._product_id = product_id
#         self._name = name
#         self._price = price

#     @property
#     def product_id(self):
#         """Getter for the immutable product_id."""
#         return self._product_id

#     @property
#     def name(self):
#         """Getter for the immutable name."""
#         return self._name

#     @property
#     def price(self):
#         """Getter for the immutable price."""
#         return self._price

#     def display_details(self):
#         """Displays product details."""
#         print(f"--- Product Details ---")
#         print(f"ID: {self.product_id}")
#         print(f"Name: {self.name}")
#         print(f"Price: ${self.price:.2f}")

