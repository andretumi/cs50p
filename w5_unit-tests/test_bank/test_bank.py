from bank import value


def test_hello():
    assert value("HELLO!") == 0
    assert value("hello there") == 0


def test_h():
    assert value("hi") == 20
    assert value("howdy") == 20
    assert value("h3ll0") == 20


def test_greeting():
    assert value("GOOD MORNING  ...") == 100
    assert value("Evening sir") == 100
