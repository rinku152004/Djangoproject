from Notifications.Notifier_Base import Notifier

class Email(Notifier):
    def send_notification(self, message):
        print(f"EMAIL SENT: {message}")

























# from Notifications.Notifier_Base import Notifier
# class Email(Notifier):
#     @property
#     def send_notification(self, customer, message):
#         print(f"[EMAIL Sent to {customer}]: {message}")

