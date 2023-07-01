class Snack:
    def __init__(self, snack_id, name, price, availability=True):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = {}
        self.sales_records = {}

    def add_snack(self, snack_id, name, price):
        if snack_id in self.inventory:
            print("Snack with the same ID already exists.")
        else:
            snack = Snack(snack_id, name, price)
            self.inventory[snack_id] = snack
            print("Snack added to the inventory.")

    def remove_snack(self, snack_id):
        if snack_id in self.inventory:
            del self.inventory[snack_id]
            print("Snack removed from the inventory.")
        else:
            print("Snack not found in the inventory.")

    def update_availability(self, snack_id, availability):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            snack.availability = availability
            print("Availability updated.")
        else:
            print("Snack not found in the inventory.")

    def record_sale(self, snack_id):
        if snack_id in self.inventory:
            snack = self.inventory[snack_id]
            if snack.availability:
                if snack_id in self.sales_records:
                    self.sales_records[snack_id] += 1
                else:
                    self.sales_records[snack_id] = 1
                print("Sale recorded.")
            else:
                print("Snack is not available.")
        else:
            print("Snack not found in the inventory.")

    def display_inventory(self):
        print("Snack Inventory:")
        print("ID\tName\t\tPrice\tAvailability")
        for snack_id, snack in self.inventory.items():
            availability = "Yes" if snack.availability else "No"
            print(f"{snack_id}\t{snack.name}\t\t{snack.price}\t{availability}")

    def display_sales_records(self):
        print("Sales Records:")
        print("ID\tName\t\tPrice\tQuantity")
        for snack_id, quantity in self.sales_records.items():
            snack = self.inventory[snack_id]
            print(f"{snack_id}\t{snack.name}\t\t{snack.price}\t{quantity}")


# Creating an instance of Canteen
canteen = Canteen()

# Adding snacks to the inventory
canteen.add_snack("1", "Chips", 10)
canteen.add_snack("2", "Chocolate", 20)
canteen.add_snack("3", "Cookie", 15)

# Displaying the inventory
canteen.display_inventory()

# Updating the availability of a snack
canteen.update_availability("2", False)

# Recording a sale
canteen.record_sale("1")
canteen.record_sale("2")
canteen.record_sale("2")

# Displaying the sales records
canteen.display_sales_records()

# Removing a snack from the inventory
canteen.remove_snack("3")

# Displaying the inventory after removal
canteen.display_inventory()
