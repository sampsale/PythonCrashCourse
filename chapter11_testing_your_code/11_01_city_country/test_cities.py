
import unittest
from city_functions import city_country

class CityCountryTests(unittest.TestCase):
    # test that function works properly
    def test_city_country(self):
        city = city_country('helsinki', 'finland')
        self.assertEqual(city, 'Helsinki, Finland')

unittest.main()