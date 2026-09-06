from twttr import shorten


def test_twttr():
    assert shorten("aeiou") == ''
    assert shorten("AEIOU") == ''
    assert shorten("TWITTER") == "TWTTR"


def test_numbers():
    assert shorten("123") == "123"
    assert shorten("4310") == "4310"
    assert shorten("h3ll0 W0RLD5") == "h3ll0 W0RLD5"


def test_punctuations():
    assert shorten("h@llo w*rld!") == "h@ll w*rld!"
