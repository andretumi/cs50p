import pytest
from jar import Jar


def test_init():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(10)
    jar.withdraw(2)
    assert str(jar) == ""


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(100)


def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(100)
