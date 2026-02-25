from Notifications.Notifier_Base import Notifier

class SMS(Notifier):
    def send_notification(self, message):
        print(f"SMS SENT: {message}")

























# from Notifications.Notifier_Base import Notifier
# class SMS(Notifier):
#     @property
#     def send_notification(self, customer, message):
#         print(f"[SMS Sent to {customer}]: {message}")
