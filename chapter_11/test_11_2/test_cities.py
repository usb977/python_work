from city_functions import city_func

def test_city_country():
    name = city_func('santiage','chile')
    assert name == 'Santiage, Chile'

def test_city_country_population():
    name = city_func('santiage','chile',5000000)
    assert name == 'Santiage, Chile - population 5000000'