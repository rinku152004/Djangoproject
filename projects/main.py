from Users.Admin import Admin
from Users.Customer import Customer
from Products.Product import Product 
from Orders.Order_Service import Order_Service
# from Orders.Orders import Orders
from Payments.UPI import UPI
from Payments.Card import Card
from Payments.Netbanking import NetBanking
from Notifications.Email import Email
from Notifications.SMS import SMS


def is_valid_gmail(email):
    return email.endswith("@gmail.com")

# Product List
product_list = [
    Product(1, "Laptop", 50000),
    Product(2, "Mouse", 500),
    Product(3, "Keyboard", 1500),
    Product(4,"Touchpad",5000)]

order_service = Order_Service()
admin = Admin(1, "Admin", "admin@gmail.com")

print("------ Shopping System ------")

while True:
    print("\n1. Login as Customer")
    print("2. Login as Admin")
    print("3. Exit")

    role = int(input("Enter choice: "))

    # ---------------- CUSTOMER ----------------
    if role == 1:
        name = input("Enter your name: ")
        while True:
            email = input("Enter your gmail: ")
            if is_valid_gmail(email):
                break
            else:
                print("Invalid Gmail! Please enter valid @gmail.com")

        customer = Customer(10, name, email)

        print("\nAvailable Products:")
        for p in product_list:
            print(f"{p.product_id}. {p.name} - ₹{p.price}")

        selected_products = []

        while True:
            pid = int(input("Enter product id to add (0 to stop): "))
            if pid == 0:
                break

            for p in product_list:
                if p.product_id == pid:
                    selected_products.append(p)
                    print(p.name, "added")

        order = customer.place_order(order_service, selected_products)
        print("Order created with ID:", order.order_id)
        # print(display_)

        print("\nChoose Payment:")
        print("1. UPI")
        print("2. Card")
        print("3. NetBanking")
        ch = int(input("Enter choice: "))

        if ch == 1:
            upi_id=input("Enter your UPI id:")
            payment = UPI(upi_id)
        elif ch == 2:
            # card_number=int(input("Enter your card number:"))
            # cvv=int(input("Enter your cvv number:"))
            payment = Card()
        else:
            bank_name=input("Enter your bank name:")
            # if bank_name.replace(" ", "").isalpha():
            #     payment = NetBanking(bank_name)
            # print("Invalid input! Please enter a name using only letters (no numbers).")
            payment = NetBanking(bank_name)

        order_service.process_payment(order, payment)

        print("\nChoose Notification:")
        print("1. Email")
        print("2. SMS")
        n = int(input("Enter choice: "))

        if n == 1:
            notifier = Email()
        else:
            notifier = SMS()

        order_service.send_notification(notifier,"Your order placed successfully!")

         # Cancel Order Option
        print("\nDo you want to cancel order?")
        print("1. Yes")
        print("2. No")

        cancel_choice = int(input("Enter choice: "))

        if cancel_choice == 1:
            success = order_service.cancel_order(order.order_id)
            if success:
                print("Order cancelled successfully!")
            else:
                print("Unable to cancel order!")

    # ---------------- ADMIN ----------------
    elif role == 2:
        orders = admin.view_all_orders(order_service.orders)
        if len(orders) == 0:
            print("\nNo orders found.")
        else:
            print("\n--- ALL ORDERS ---")
            for o in orders:
                print(
                    f"\n--- Order Summary (ID: {o.order_id}) ---\n"
                    f"OrderID:{o.order_id} \n"
                    f"Customer:{o.customer.name}\n"
                    f"Total:{o.calculate_total():.2f}\n"
                    f"Status:{o.status}"
                )
                # print(f"\n--- Order Summary (ID: {o.order_id}) ---")
                # print(f"Customer:{o.customer.name}")
                # print(f"Status: {o.status.name}")
                # print(f"Items: {[p.name for p in o._products]}")
                # print(f"Total: ${o.calculate_total():.2f}")


    elif role == 3:
        print("Exitingggg system...")
        break

    else:
        print("Invalid choice")
