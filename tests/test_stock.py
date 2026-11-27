import pytest

from inventory.stock import Stock


def test_add_and_total():
    s = Stock()
    s.add("a", 2)
    s.add("b", 3)
    assert s.total() == 5


def test_remove_too_much():
    s = Stock()
    s.add("a", 1)
    with pytest.raises(ValueError):
        s.remove("a", 2)
