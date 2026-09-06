import pytest
from seasons import to_text


def test_minutes_alive():
    assert to_text("2001") == "Two thousand one minutes"
    assert to_text("1994") == "One thousand, nine hundred ninety-four minutes"
    assert to_text("999") == "Nine hundred ninety-nine minutes"
