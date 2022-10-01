import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for each module in Class Employee"""

    def setUp(self):
        """
        Create an employee and a set of responses for use in all test methods.
        """
        self.employee = Employee(first_name="Sam", last_name="Smith", salary=50000)

    def test_give_default_raise(self):
        """Test that a default raise is given properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custom_raise(self):
        """Test that a custom raise is given properly."""
        self.employee.give_raise(amount=10000)
        self.assertEqual(self.employee.salary, 60000)