from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        """All payment methods must implement this method"""
        pass
























# class PaymentMethod:
#     def pay(self, amount):
#         self.amount=amount

# # --- Payment Module (Abstraction + Polymorphism) ---
# from Payments import Card, UPI, Netbanking
# class PaymentMethod(Card, UPI, Netbanking):
#     """Abstract Base Class (ABC) defining the common interface."""
#     # @abstractmethod
#     def process_payment(self, amount):
#         self.amount=amount
