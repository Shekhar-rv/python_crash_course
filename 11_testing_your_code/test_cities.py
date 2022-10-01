import unittest
from cities import city_country

class TestCitiesFunction(unittest.TestCase):
    """Testing the 'cities.py'"""

    def test_city_country(self):
        """Verifying thet city and country names are formatted
           correctly."""
        formatted_location_name = city_country(city="sheffield", country="united kingdom")
        self.assertAlmostEqual(formatted_location_name, "Sheffield, United Kingdom")

    def test_city_country_population(self):
        """Verifying thet city and country names and population are formatted
           correctly."""
        formatted_location_data = city_country(city='sheffield', country='united kingdom', population=240050)
        self.assertAlmostEqual(formatted_location_data, "Sheffield, United Kingdom - Population 240050")

unittest.main()