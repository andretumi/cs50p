from plates import is_valid


# All vanity plates must start with at least two letters.
def test_start_2_letters():
    assert is_valid("HI123") == True
    assert is_valid("HELLO") == True
    assert is_valid("A12345") == False
    assert is_valid("123456") == False


# Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters(letters).
def test_valid_length():
    assert is_valid("HI") == True
    assert is_valid("BOTTLE") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGHIKLMN") == False


# Numbers cannot be used in the middle of a plate(AAA22A); they must come at the end (AAA222).
def test_numbers_at_end():
    assert is_valid("ABC123") == True
    assert is_valid("HIP30") == True
    assert is_valid("123ABC") == False
    assert is_valid("ABC5DE") == False


# The first number used cannot be a ‘0’.
def test_first_num_non_zero():
    assert is_valid("HELI05") == False
    assert is_valid("AB0123") == False


# No periods, spaces, or punctuation marks are allowed.
def test_valid_chars():
    assert is_valid("CS.50") == False
    assert is_valid("") == False
