class menu:
    def __init__(self):
        self.items = []

    def add_item(self,item):
        self.items.append(item)
        print(f"{item.name} added successfully to menu!")

    def find_item(self,item_name):
        for i in self.items:
            if i.name.lower() == item_name.lower():
                return i
        return None
    
    def remove_item(self,item_name):
        x = self.find_item(item_name)
        if x:
            self.items.remove(x)
            print(f"{x.name} removed successfully to menu!")
        else:
            print("Item does not exict")

    def show_item(self):
        print(f"Name\tPrice\tQuantity")
        for x in self.items:
            print(f"{x.name}\t{x.price}\t{x.quantity}")
