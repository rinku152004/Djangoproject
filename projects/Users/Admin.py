from Users.Users import Users

class Admin(Users):
    def view_all_orders(self, orders):
        try:
            return orders
        except Exception as e:
            print(f"An error occurred while viewing orders: {e}")
            # You might want to raise the exception again or return None/False
            return None
        





























# from Users import Users
# # class Admin(User):
# #     def __init__(self):
# #         super().__init__()
# class Admin(Users):
#     """
#     Admin user class, inheriting from User.
#     Additional functionality: Can view all orders.
#     """
#     def __init__(self, user_id, name, email):
#         # Call the parent class constructor using super() to initialize common properties
#         super().__init__(user_id, name, email)

#     def view_all_orders(self):
#         """Admin functionality to view all orders."""
#         print(f"Admin {self.name} is viewing all system orders.")