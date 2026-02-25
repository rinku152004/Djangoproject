from abc import ABC, abstractmethod
class Notifier(ABC):
    """Abstract interface for notification services."""
    @abstractmethod
    def send_notification(self, message):
        # self.message=message
        pass


























# from abc import ABC, abstractmethod
# class Notifier:
#     """Abstract interface for notification services."""
#     @abstractmethod
#     def send_notification(self, customer,message):
#         self.customer=customer
#         self.message=message
