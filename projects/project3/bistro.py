from datastructures.bag import Bag
from datastructures.linkedlist import LinkedList
from datastructures.liststack import ListStack
from datastructures.circularqueue import CircularQueue
from datastructures.deque import Deque
from dataclasses import dataclass
from typing import List

""" all classes are just in this one file, and program is very minimal"""

@dataclass #idk if this is needed... but its fun to type!
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.size = "Medium"

@dataclass
class OrderItem:
    def __init__(self, drink, customizations=""):
        self.drink = drink
        self.customizations = customizations

    def __str__(self):
        return f"Medium {self.drink} with {self.customizations}"

@dataclass
class CustomerOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order = LinkedList[OrderItem](data_type = OrderItem)
    
    def add_item(self, item):
        self.order.append(item)

    def display(self):
        print(f"Order for {self.customer_name}")
        for item in self.order:
            print(f"- {item}")

@dataclass
class BistroSystem:
    def __init__(self):
        self.menu = Bag[Drink]()
        self.open_orders = CircularQueue[CustomerOrder](maxsize=10, data_type=CustomerOrder) # Example capacity
        self.completed_orders = Deque[CustomerOrder](data_type=CustomerOrder)
        self.initialize_menu()

    def initialize_menu(self):
        self.menu.add(Drink("Latte", 5.00))
        self.menu.add(Drink("Chai Latte", 5.00))
        self.menu.add(Drink("Lemonade", 4.00))
        self.menu.add(Drink("Matcha", 6.00))
        self.menu.add(Drink("Hote Tea", 4.00))

    def display_menu(self):
        print("\n 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧")
        for i, drink in enumerate(self.menu.items): 
            print(f"{i+1}. {drink.name} (Medium) - ${drink.price:.2f}")
        print("-------------------\n")

    def new_order(self):
        customer_name = input("Enter customer name: ")
        current_order = CustomerOrder(customer_name)

        while True:
            self.display_menu()
            try:
                choice = input("Enter the number of the drink to order (or 'done'): ")
                if choice.lower() == 'done':
                    break
                choice = int(choice)
                if 1 <= choice <= len(self.menu.items): # Use len on the items list
                    selected_drink = self.menu.items[choice - 1] # Access by index
                    customization = input(f"Enter customization for {selected_drink.name} (optional): ")
                    order_item = OrderItem(selected_drink, customization)
                    current_order.add_item(order_item)
                else:
                    print("That's not on the menu!.")
            except ValueError:
                print("Invalid answer. Please enter a number or 'done'!")

        print("\n--- Order Confirmation ---")
        current_order.display()
        confirm = input("Confirm order? (yes/no): ").lower()
        if confirm == 'yes':
            if self.open_orders.full:
                print("Open orders queue is full. Please wait.")
            else:
                self.open_orders.enqueue(current_order)
                print(f"Order for {customer_name} added to the queue.")
        else:
            print("Order cancelled.")

    def view_open_orders(self):
        print("\n--- Open Orders ---")
        if self.open_orders.empty:
            print("No open orders.")
        else:
            temp_queue = CircularQueue[CustomerOrder](maxsize=self.open_orders.maxsize, data_type=CustomerOrder)
            while not self.open_orders.empty:
                order = self.open_orders.dequeue()
                print(f"- {order.customer_name}: ", end="")
                drink_summary = ", ".join([item.drink.name for item in order.order])
                print(drink_summary)
                temp_queue.enqueue(order)
            while not temp_queue.empty:
                self.open_orders.enqueue(temp_queue.dequeue())
        print("---------------------\n")

    def mark_next_order_complete(self):
        if self.open_orders.empty:
            print("No orders in the queue to complete.")
        else:
            completed_order = self.open_orders.dequeue()
            self.completed_orders.enqueue(completed_order) # moving to back of deque, but keeping for end of day recap
            print(f"Order for {completed_order.customer_name} marked as complete.")

    def view_end_of_day_report(self):
        print("\n--- Daily Report ---")
        drink_counts = {}
        total_revenue = 0.0

        for order in self.completed_orders: 
            for item in order.order: 
                drink_name = item.drink.name
                price = item.drink.price
                drink_counts[drink_name] = drink_counts.get(drink_name, 0) + 1
                total_revenue += price

        if not drink_counts:
            print("No orders completed today.")
            return

        print("--- Drinks Sold ---")
        for drink, count in drink_counts.items():
            price = next((d.price for d in self.menu.items if d.name == drink), 0.0)
            total_sales = count * price
            print(f"- {drink}: {count} (Total Sales: ${total_sales:.2f})")

        print(f"\n--- Total Revenue ---: ${total_revenue:.2f}")
        print("-------------------------\n")

    def run(self):
        while True:
            print("\n--- Welcome to Addison's Bistro! ---")
            print("1. Display Menu")
            print("2. Take New Order")
            print("3. View Open Orders")
            print("4. Mark Next Order as Complete")
            print("5. View End-of-Day Report")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.new_order()
            elif choice == '3':
                self.view_open_orders()
            elif choice == '4':
                self.mark_next_order_complete()
            elif choice == '5':
                self.view_end_of_day_report()
            elif choice == '6':
                print("Thank you for using Addison's Bistro system!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    bistro_system = BistroSystem()
    bistro_system.run()
