class Item:
    #Class represents items to be placed in the shopping cart

    def __init__(self, name, price, quantity): #defining class attributes
        self.name = name
        self.price = price
        self.quantity = quantity

class POS:
    #Point of Sale system implemented

    def __init__(self):
        # Retail store catalog with products available
        self.catalog = {
            "fan": [130, 10],
            "Bread": [50, 20],
            "Rice": [20, 15],
            "Eggs": [50, 8],
            "soft soda" : [10.99, 12],
            "water" : [6.01, 100],
            "mattress" : [425.20, 90],
            "laptop" : [15.50, 50],
            "flour" : [18.95, 5],
            "carrot" : [5.10, 60],
            "television" : [345,20],
            
        }
        self.cart = []  # Cart used to store products

    def view_items(self):
        print("Available items in catalog:")
        for item, (price, stock) in self.catalog.items():
            print(f"{item.title()}: ${price:.2f} - {stock} in stock")

    def add_item(self, name, qty): #Function used to add items in the cart

        if name not in self.catalog:
            print("Item not found!")
            return

        price, stock = self.catalog[name]

        if qty > stock:
            print(f"Only {stock} left in stock.")
            return

        self.cart.append(Item(name, price, qty))
        self.catalog[name][1] -= qty
        print(f"Added {qty} {name} to cart.")

    def remove_item(self, name): #Function used to remove items from the cart

        for item in self.cart:
            if item.name == name:
                self.catalog[name][1] += item.quantity
                self.cart.remove(item)
                print(f"Removed {name} from cart.")
                return

        print("Item not in cart.")

    def show_cart(self):
        #Function used to display items in the cart
        if not self.cart:
            print("Cart is empty.")
            return

        print("Cart items:")
        for item in self.cart:
            print(f"{item.name} - {item.quantity} x {item.price}")

    def checkout(self):
        #payment process
        if not self.cart:
            print("Cart is empty! Add items first.")
            return

        subtotal = sum(item.price * item.quantity for item in self.cart)
        discount = subtotal * 0.05 if subtotal > 5000 else 0
        tax = (subtotal - discount) * 0.15
        total = subtotal - discount + tax

        # Displaying receipt info
        print("\n--- Checkout ---")
        print(f"Subtotal: {subtotal}")
        if discount:
            print(f"Discount: -{discount}")
        print(f"Tax: +{tax}")
        print(f"Total: {total}")

        # Handle payment input
        while True:
            try:
                payment = float(input("Enter payment: "))
                if payment < total:
                    print("Not enough money!")
                else:
                    break
            except ValueError:
                print("Invalid input!")

        # Receipt generation
        change = payment - total
        print(f"Payment: {payment}")
        print(f"Change: {change}")
        print("Thank you for shopping!")

        self.cart.clear()  # Clear cart after purchase



# Implementing POSSYTEM
pos = POS()

while True: #Loop
    print("\n1. View Items \n2. Add Item\n3. Remove Item\n4. View Cart\n5. Checkout\n6. Exit") #Menu Options
    choice = input("Choose an option: ")

    if choice == "1":
        pos.view_items()

    if choice == "2":
        item = input("Enter item name: ")
        try:
            qty = int(input("Enter quantity: "))
            pos.add_item(item, qty)
        except ValueError:
            print("Invalid quantity!")
    elif choice == "3":
        item = input("Enter item name to remove: ")
        pos.remove_item(item)
    elif choice == "4":
        pos.show_cart()
    elif choice == "5":
        pos.checkout()
    elif choice == "6":
        print("Thanks for stopping by!")
        break
    else:
        print("Invalid choice!")