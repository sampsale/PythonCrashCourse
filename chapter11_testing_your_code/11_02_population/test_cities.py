
import unittest
from city_functions import city_country

# inherit from testcase class and make test class
class CityCountryTests(unittest.TestCase):
    # test that function works with city and country only
    def test_city_country(self):
        city = city_country('helsinki', 'finland')
        self.assertEqual(city, 'Helsinki, Finland')
    # test that function works with additional argument population
    def test_city_country_population(self):
        city = city_country('helsinki', 'finland', 5_000_000)
        self.assertEqual(city, 'Helsinki, Finland - population 5000000')

unittest.main()