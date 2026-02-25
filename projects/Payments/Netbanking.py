from Payments.Payment_Base import PaymentMethod

class NetBanking(PaymentMethod):
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def pay(self, amount):
        print(f"Redirecting to {self.bank_name} portal for ₹{amount} payment")
        return True




















# from Payments import Payment_Base
# class NetBankingPayment(Payment_Base):
#     def process_payment(self, amount):
#         return f"Processing NetBanking payment of ${amount:.2f}."


# class NetBanking(PaymentMethod):
#     def pay(self, amount):
#         print(f"NetBanking Payment of ₹{amount} successful")
#         return True
