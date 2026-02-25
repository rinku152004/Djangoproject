from Orders.Orders import Orders

class Order_Service:
    def __init__(self):
        self.orders = []
        self.counter = 1

    def create_order(self, customer, products):
        order = Orders(self.counter, customer, products)
        self.orders.append(order)
        self.counter += 1
        return order

    def process_payment(self, order, payment_method):
        amount = order.calculate_total()
        # payment_method could be UPI, CreditCard, or NetBanking
        success = payment_method.pay(amount) 

        if success:
            order.set_status("PAID")
            return True
        return False
    
    def send_notification(self, notifier, message):
        notifier.send_notification(message)

    def cancel_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                order.set_status("CANCELLED")
                return True
        return False
    

