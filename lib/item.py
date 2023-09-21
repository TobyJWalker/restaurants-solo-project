class Item():
    def __init__(self, name, price):
        if type(name) != str:
            raise TypeError("name must be a string")
        elif name.strip() == "":
            raise ValueError("name must not be empty")
        elif type(price) != float and type(price) != int:
            raise TypeError("price must be a number")
        elif price < 0:
            raise ValueError("price must be positive")
        
        self.name = name
        self.price = float(f'{price:.2f}')