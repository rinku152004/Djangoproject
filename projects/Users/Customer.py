from Users.Users import Users

class Customer(Users):
    def place_order(self, order_service, products):
        try:
            return order_service.create_order(self, products)
        except Exception as e:
            print(f"An error occurred while placing order: {e}")
            # You might want to raise the exception again or return None/False
            return None 