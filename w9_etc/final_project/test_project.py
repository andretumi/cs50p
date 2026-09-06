import pytest
from project import scrape_data, notify_user, valid_url


urls = ("https://www.shopstar.pe/agua-de-mesa-san-luis-sin-gas-bidon-7l-785599/p",
        "https://www.shopstar.pe/repelente-de-insectos-en-aerosol-off--family-frasco-217ml-1314052/p",
        "https://www.shopstar.pe/pelotas-de-futbol-new-athletic-premium-size-5-negro-con-blanco-1475638/p",
        "https://www.shopstar.pe/",
        "NOT A URL")


def test_scrape_data():
    assert scrape_data(urls[0]) == ("Agua de Mesa SAN LUIS Sin Gas Bidón 7L", 7)
    assert scrape_data(urls[1]) == ("Repelente de Insectos en Aerosol OFF! Family Frasco 217ml", 23)
    assert scrape_data(urls[2]) == ("PELOTAS DE FUTBOL NEW ATHLETIC PREMIUM SIZE 5 NEGRO CON BLANCO", 79)


def test_notify_user():
    assert notify_user(100, 100) == True
    assert notify_user(50, 100) == True
    assert notify_user(100, 50) == False


def test_valid_url():
    assert valid_url(urls[0]) == True
    assert valid_url(urls[1]) == True
    assert valid_url(urls[2]) == True
    with pytest.raises(SystemExit) as e:
        assert valid_url(urls[3])
    assert e.value.code == "Invalid URL"
    with pytest.raises(SystemExit) as e:
        assert valid_url(urls[4]) == False
    assert e.value.code == "Invalid URL"
