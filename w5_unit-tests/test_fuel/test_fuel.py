from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("30/100") == 30


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_exceptions():
    with pytest.raises(ValueError):
        convert("one/two")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
