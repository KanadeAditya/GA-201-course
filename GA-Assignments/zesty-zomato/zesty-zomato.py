# Zesty Zomato Command-Line System

# Function to display the menu
def display_menu(menu):
    print("Zesty Zomato Menu:")
    print("ID\tDish Name\tPrice\tAvailability")
    for dish_id, dish in menu.items():
        print(f"{dish_id}\t{dish['name']}\t\t${dish['price']}\t{dish['availability']}")
    print()

# Function to add a dish to the menu
def add_dish(menu, dish_id, dish_name, price):
    menu[dish_id] = {'name': dish_name, 'price': price, 'availability': 'yes'}
    print(f"{dish_name} added to the menu.")
    print()

# Function to remove a dish from the menu
def remove_dish(menu, dish_id):
    if dish_id in menu:
        dish_name = menu[dish_id]['name']
        del menu[dish_id]
        print(f"{dish_name} removed from the menu.")
    else:
        print("Invalid dish ID. Please try again.")
    print()

# Function to update the availability of a dish
def update_availability(menu, dish_id, availability):
    if dish_id in menu:
        menu[dish_id]['availability'] = availability
        print("Availability updated.")
    else:
        print("Invalid dish ID. Please try again.")
    print()

# Function to take a new order
def take_order(menu, orders, order_id, customer_name, dish_ids):
    order = {'customer_name': customer_name, 'status': 'received', 'dishes': []}
    for dish_id in dish_ids:
        if dish_id in menu and menu[dish_id]['availability'] == 'yes':
            order['dishes'].append(menu[dish_id]['name'])
        else:
            print(f"Dish ID {dish_id} is not available. Order cannot be processed.")
            return
    orders[order_id] = order
    print("Order placed successfully.")
    print()

# Function to update the status of an order
def update_order_status(orders, order_id, status):
    if order_id in orders:
        orders[order_id]['status'] = status
        print("Order status updated.")
    else:
        print("Invalid order ID. Please try again.")
    print()

# Function to review all orders
def review_orders(orders):
    print("Zesty Zomato Orders:")
    if len(orders) == 0:
        print("No orders to review.")
    else:
        for order_id, order in orders.items():
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {order['customer_name']}")
            print(f"Status: {order['status']}")
            print("Dishes:")
            for dish in order['dishes']:
                print(f"- {dish}")
            print()
    print()

# Function to validate integer inputs
def validate_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Function to validate floating-point inputs
def validate_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program loop
def main():
    menu = {}
    orders = {}
    order_id = 1

    while True:
        print("Welcome to Zesty Zomato!")
        print("1. Display Menu")
        print("2. Add Dish to Menu")
        print("3. Remove Dish from Menu")
        print("4. Update Dish Availability")
        print("5. Take Order")
        print("6. Update Order Status")
        print("7. Review Orders")
        print("8. Exit")

        choice = validate_integer_input("Enter your choice (1-8): ")

        if choice == 1:
            display_menu(menu)
        elif choice == 2:
            dish_id = validate_integer_input("Enter dish ID: ")
            dish_name = input("Enter dish name: ")
            price = validate_float_input("Enter price: $")
            add_dish(menu, dish_id, dish_name, price)
        elif choice == 3:
            dish_id = validate_integer_input("Enter dish ID to remove: ")
            remove_dish(menu, dish_id)
        elif choice == 4:
            dish_id = validate_integer_input("Enter dish ID to update availability: ")
            availability = input("Enter availability (yes/no): ")
            update_availability(menu, dish_id, availability)
        elif choice == 5:
            customer_name = input("Enter customer name: ")
            dish_ids = []
            while True:
                dish_id = validate_integer_input("Enter dish ID (0 to stop): ")
                if dish_id == 0:
                    break
                dish_ids.append(dish_id)
            take_order(menu, orders, order_id, customer_name, dish_ids)
            order_id += 1
        elif choice == 6:
            order_id = validate_integer_input("Enter order ID to update status: ")
            status = input("Enter new status: ")
            update_order_status(orders, order_id, status)
        elif choice == 7:
            review_orders(orders)
        elif choice == 8:
            print("Thank you for using Zesty Zomato. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")
        print()

# Run the program
# if __name__ == "__main__":
main()
