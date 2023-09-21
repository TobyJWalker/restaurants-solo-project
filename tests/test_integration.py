from lib.order import *
from twilio.rest import Client
import pytest

def test_total_cost_one_item():
    order = Order(Client)
    item = Item("pizza", 3.00)
    order.add_item(item)
    assert order.total_cost() == 3.00

def test_total_cost_two_items():
    order = Order(Client)
    item1 = Item("pizza", 3.00)
    item2 = Item("chips", 1.00)
    order.add_item(item1)
    order.add_item(item2)
    assert order.total_cost() == 4.00

def test_receipt_one_item():
    order = Order(Client)
    item = Item("pizza", 3.00)
    order.add_item(item)
    assert order.receipt() == "pizza - £3.00\nTotal: £3.00"

def test_receipt_two_items():
    order = Order(Client)
    item1 = Item("pizza", 3.00)
    item2 = Item("chips", 1.00)
    order.add_item(item1)
    order.add_item(item2)
    assert order.receipt() == "pizza - £3.00\nchips - £1.00\nTotal: £4.00"

def test_text_non_existent_number():
    order = Order(Client)
    item1 = Item("pizza", 3.00)
    item2 = Item("chips", 1.00)
    order.add_item(item1)
    order.add_item(item2)

    with pytest.raises(ValueError) as e:
        order_output = order.place_order("+440123456789")
    assert str(e.value) == "number must be a valid number"

def test_text():
    order = Order(Client)
    item1 = Item("pizza", 3.00)
    item2 = Item("chips", 1.00)
    order.add_item(item1)
    order.add_item(item2)

    assert order.items == [item1, item2]
    assert order.receipt() == "pizza - £3.00\nchips - £1.00\nTotal: £4.00"

    order_output = order.place_order("+447481832146")
    assert order_output == "Order is being prepared"