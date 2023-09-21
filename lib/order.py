from lib.item import Item
from lib.menu import Menu
from twilio.rest import Client
from datetime import datetime, timedelta
import os


ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_NUMBER = os.environ["TWILIO_ACCOUNT_NUMBER"]

class Order():
    def __init__(self, client):
        self.items = []
        self.client = client

    def add_item(self, item):
        if type(item) != Item:
            raise TypeError("item must be instance of Item")
        self.items.append(item)
    
    def total_cost(self):
        if self.items == []:
            return 0
        else:
            return sum([item.price for item in self.items])

    def receipt(self):
        if self.items == []:
            return "Order is empty"
        else:
            return "\n".join([f"{item.name} - £{item.price:.2f}" for item in self.items]) + f"\nTotal: £{self.total_cost():.2f}"

    def _text(self, number):
        expected_time = datetime.now() + timedelta(minutes=30)
        formatted_time = expected_time.strftime("%H:%M")

        client = self.client(ACCOUNT_SID, AUTH_TOKEN)

        try:
            message = client.messages.create(
                body=f"Order placed, delivery will be by {formatted_time}",
                from_=TWILIO_NUMBER,
                to=number,
            )
        except:
            raise ValueError("number must be a valid number")

        return message.status

    def place_order(self, number):
        if type(number) != str:
            raise TypeError("number must be a string")
        elif len(number) != 13:
            raise ValueError("number must be 13 digits (with +44)")
        elif number[:3] != "+44":
            raise ValueError("number must be a UK number (+44)")
        elif self.items == []:
            raise ValueError("Order is empty")

        else:
            response = self._text(number)
            if response == "queued":
                return "Order is being prepared"
            else:
                return "Order failed"
        