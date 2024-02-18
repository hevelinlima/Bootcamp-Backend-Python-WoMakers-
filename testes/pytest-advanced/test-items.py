import pytest


@pytest.mark.parametrize("item", ["0", "1", "10", "33", "11"])
def test_string_is_digit(item):
    assert item.isdigit()
