class Orders:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id
        self.customer = customer
        self.products = products
        self.status = "CREATED"

    def calculate_total(self):
        return sum(p.price for p in self.products)
        # total = sum(product.price for product in self._products)
        # return total

    def set_status(self, status):
        self.status = status
        







        







# # order_module.py

# from Products import Product  # Assumes product_module.py exists from a previous step
# from enum import Enum, auto

# class OrderStatus(Enum):
#     """Enumeration for maintaining order status."""
#     CREATED = auto()
#     PAID = auto()
#     CANCELLED = auto()

# class Order:
#     """
#     Represents a customer order.
#     Uses composition: an Order has a list of Products.
#     """
#     def __init__(self, order_id, customer_email):
#         self.order_id = order_id
#         self.customer_email = customer_email
#         self._products = []  # Composition link
#         self.status = OrderStatus.CREATED

#     def add_product(self, product: Product):
#         """Adds a product to the order."""
#         if self.status == OrderStatus.CREATED:
#             self._products.append(product)
#             print(f"Added '{product.name}' to Order {self.order_id}.")
#         else:
#             print(f"Cannot add products to an order that is {self.status.name}.")

#     def calculate_total(self):
#         """Calculates the total cost dynamically."""
#         total = sum(product.price for product in self._products)
#         return total

#     def set_status(self, new_status: OrderStatus):
#         """Updates the order status."""
#         self.status = new_status
#         print(f"Order {self.order_id} status updated to {self.status.name}.")

    # def display_order_summary(self):
    #     """Displays a summary of the order."""
    #     print(f"\n--- Order Summary (ID: {self.order_id}) ---")
    #     print(f"Status: {self.status.name}")
    #     print(f"Items: {[p.name for p in self._products]}")
    #     print(f"Total: ${self.calculate_total():.2f}")
