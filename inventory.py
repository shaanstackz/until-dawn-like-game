class Inventory:
    def __init__(self):
        self.items = {
            "gun": False,
            "flashlight": False,
            "key": False
        }

    def add_item(self, item_name):
        if item_name in self.items:
            self.items[item_name] = True
            print(f"You have acquired a {item_name}.")

    def has_item(self, item_name):
        return self.items.get(item_name, False)
