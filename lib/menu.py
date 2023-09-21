from lib.item import Item

class Menu():
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        if type(item) != Item:
            raise TypeError("item must be instance of Item")
        self.items.append(item)

    def get_menu(self):
        if self.items == []:
            return "Menu is empty"
        
        return "\n".join([f"{item.name} - £{item.price:.2f}" for item in self.items])