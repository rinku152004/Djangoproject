from Payments.Payment_Base import PaymentMethod

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Processing UPI payment of ₹{amount} via ID: {self.upi_id}")
        return True  # Simulating a successful transaction
























# class UPI(PaymentMethod):
#     def pay(self, amount):
#         print(f"UPI Payment of ₹{amount} successful")
#         return True


# from Payments import Payment_Base
# class UPIPayment(Payment_Base):
#     def process_payment(self, amount):
#         return f"Processing UPI payment of ${amount:.2f}."
