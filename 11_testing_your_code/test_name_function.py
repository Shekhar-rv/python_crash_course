import unittest
from name_function import get_formatted_name


class TestNameFunction(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """verifying that names with only a first and last name are
        formatted correctly"""
        formatted_name = get_formatted_name(first="shekhar", last="ramesh")
        self.assertEqual(formatted_name, "Shekhar Ramesh")

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            first="wolfgang", last="mozart", middle="amadeus"
        )
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")


unittest.main()
