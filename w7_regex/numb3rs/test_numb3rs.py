from numb3rs import validate


def testing_ipv4():
    assert validate("172.16.31.50") == True
    assert validate("255.255.255.255") == True
    assert validate("300.200.100.50") == False
    assert validate("192.168.1.256") == False


def only_first_byte():
    assert validate("250.345.453.2343") == False
    assert validate("12.2434.543.2324") == False


def testing_other_bytes_but_4():
    assert validate("192.168.1") == False
    assert validate("123.123.233.231.12") == False
