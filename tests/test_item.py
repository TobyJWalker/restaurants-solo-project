from lib.item import Item
import pytest

def test_name_not_string():
    with pytest.raises(TypeError) as e:
        Item(1, 1.00)
    assert str(e.value) == "name must be a string"

def test_name_empty():
    with pytest.raises(ValueError) as e:
        Item("", 1.00)
    assert str(e.value) == "name must not be empty"

def test_name_space():
    with pytest.raises(ValueError) as e:
        Item(" ", 1.00)
    assert str(e.value) == "name must not be empty"

def test_price_not_number():
    with pytest.raises(TypeError) as e:
        Item("name", "price")
    assert str(e.value) == "price must be a number"

def test_price_negative():
    with pytest.raises(ValueError) as e:
        Item("name", -1.00)
    assert str(e.value) == "price must be positive"

def test_price_integer():
    item = Item("name", 1)
    assert item.price == 1.00

def test_item_valid():
    item = Item("name", 1.00)
    assert item.name == "name"
    assert item.price == 1.00