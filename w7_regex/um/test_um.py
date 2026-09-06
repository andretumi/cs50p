import pytest
from um import count


def test_count():
    assert count("um") == 1
    assert count("Hello, um, world.") == 1
    assert count("This is, um... CS50.") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Um, thanks, um, regular expressions make sense now.") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
    assert count("UM um uM Um") == 4
    assert count("That'sUMa test.") == 0
    assert count("Um?") == 1
    assert count("UM!") == 1
    assert count("U.m?") == 0
    assert count("U m!") == 0
