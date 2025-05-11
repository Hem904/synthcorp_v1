class InventoryManager:
    def __init__(self):
        self.inventory = {
            'lens_material': 100,
            'coating_solution': 100,
            'AR_chip': 50
        }
        self.threshold = {
            'lens_material': 20,
            'coating_solution': 20,
            'AR_chip': 10
        }

    def consume(self, item, amount):
        if item not in self.inventory:
            raise ValueError(f"Item {item} not found in inventory.")

        self.inventory[item] -= amount
        print(f"{item} used: {amount}. Remaining: {self.inventory[item]}")

        if self.inventory[item] < self.threshold[item]:
            self.reorder(item)

    def reorder(self, item):
        restock_amount = 50
        self.inventory[item] += restock_amount
        print(f"Reordered {restock_amount} units of {item}. New quantity: {self.inventory[item]}")

    def get_inventory_status(self):
        return self.inventory.copy()

    def update_inventory(self, item, quantity):
        if item not in self.inventory:
            self.inventory[item] = int(quantity)
        else:
            self.inventory[item] += int(quantity)
        print(f"Updated {item} to {self.inventory[item]}")
