import pytest
from unittest.mock import Mock
from twilio.rest import Client
from lib.order import *

def test_order_empty():
    order = Order("client")
    assert order.items == []

def test_add_non_item():
    order = Order("client")
    with pytest.raises(TypeError) as e:
        order.add_item("item")
    assert str(e.value) == "item must be instance of Item"

def test_add_item():
    order = Order("client")
    item = Item("name", 1.00)
    order.add_item(item)
    assert order.items == [item]

def test_total_cost_empty():
    order = Order("client")
    assert order.total_cost() == 0

def test_receipt_empty():
    order = Order("client")
    assert order.receipt() == "Order is empty"

def test_place_empty_order():
    order = Order("client")
    with pytest.raises(ValueError) as e:
        order.place_order("+441234567890")
    assert str(e.value) == "Order is empty"

def test_number_not_string():
    order = Order("client")
    with pytest.raises(TypeError) as e:
        order.place_order(1)
    assert str(e.value) == "number must be a string"

def test_number_incorrect_length():
    order = Order(r"client")
    with pytest.raises(ValueError) as e:
        order.place_order("+4401234")
    assert str(e.value) == "number must be 13 digits (with +44)"

def test_number_not_44():
    order = Order("client")
    with pytest.raises(ValueError) as e:
        order.place_order("1234567890123")
    assert str(e.value) == "number must be a UK number (+44)"

def test_place_order():
    client_mock = Mock(name="client")

    order = Order(client_mock)
    order._text = Mock(return_value="queued")
    item = Item("pizza", 1.00)
    order.add_item(item)
    assert order.place_order("+447481832146") == "Order is being prepared"