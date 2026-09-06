import pytest
from working import convert


def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")

    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")

    with pytest.raises(ValueError):
        assert convert("25:30 AM to 30:45 PM")

    with pytest.raises(ValueError):
        assert convert("10:70 AM to 3:45 PM")

    with pytest.raises(ValueError):
        assert convert("12 AM 12 PM")
