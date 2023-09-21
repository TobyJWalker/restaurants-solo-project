from lib.menu import Menu
from lib.item import Item
from unittest.mock import Mock
import pytest

def test_menu_empty():
    menu = Menu()
    assert menu.items == []

def test_add_non_item():
    menu = Menu()
    with pytest.raises(TypeError) as e:
        menu.add_item("item")
    assert str(e.value) == "item must be instance of Item"

def test_add_item():
    menu = Menu()
    item = Item("name", 1.00)
    menu.add_item(item)
    assert menu.items == [item]

def test_get_menu_empty():
    menu = Menu()
    assert menu.get_menu() == "Menu is empty"

def test_get_menu_one_item():
    menu = Menu()
    item = Item("Pizza", 3.00)
    menu.add_item(item)
    assert menu.get_menu() == "Pizza - £3.00"

def test_get_menu_two_items():
    menu = Menu()
    item1 = Item("Pizza", 3.00)
    item2 = Item("Chips", 1.00)
    menu.add_item(item1)
    menu.add_item(item2)
    assert menu.get_menu() == "Pizza - £3.00\nChips - £1.00"