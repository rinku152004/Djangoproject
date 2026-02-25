from Payments.Payment_Base import PaymentMethod

class Card(PaymentMethod):
    # def __init__(self,card_number,cvv):
        # self.card_number = card_number
        # self.cvv = cvv

    def pay(self, amount):
        print(f"Processing Credit Card payment of ₹{amount:.2f}.")
        return True




















# class Card(PaymentMethod):
#     def pay(self, amount):
#         print(f"Card Payment of ₹{amount} successful")
#         return True

# from Payments import Payment_Base
# class CreditCardPayment(Payment_Base):
#     def process_payment(self, amount):
#         return f"Processing Credit Card payment of ${amount:.2f}."
