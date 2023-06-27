from city_functions import city_country


def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"


def test_city_country_population():
    expected = "Santiago, Chile - population 5000000"
    assert city_country("santiago", "chile", 5000000) == expected
