
a>> PURPOSE

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

>> CLASSES

```python

class Item():
    def __init__(self, name, price):
        # PURPOSE: create a menu item with a name and price
        # INPUTS: name (string), price (float)
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: sets the name and price of the item
        pass
    

class Menu():
    def __init__(self):
        # PURPOSE: create a menu
        # INPUTS: none
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: creates an empty menu
        pass
    
    def add_item(self, item):
        # PURPOSE: add an item to the menu
        # INPUTS: item (Item)
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: adds an item to the menu
        pass

    def get_menu(self):
        # PURPOSE: return a readable list of items
        # INPUTS: none
        # OUTPUTS: none
        # RETURN: list
        # EFFECT: none
        pass

class Order():
    def __init__(self):
        # PURPOSE: create an order
        # INPUTS: none
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: creates an empty order
        pass

    def add_item(self, item):
        # PURPOSE: add an item to the order
        # INPUTS: item (Item)
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: adds an item to the order
        pass

    def receipt(self):
        # PURPOSE: return a readable receipt
        # INPUTS: none
        # OUTPUTS: none
        # RETURN: string
        # EFFECT: none
        pass

    def _text(self, number, requester):
        # PURPOSE: send a text to the number
        # INPUTS: number (string)
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: sends a text to the number with the delivery time
        pass

    def place_order(self, number):
        # PURPOSE: place the order
        # INPUTS: number (string)
        # OUTPUTS: none
        # RETURN: none
        # EFFECT: sends a text to the number with the delivery time after verfifying number
        pass

```