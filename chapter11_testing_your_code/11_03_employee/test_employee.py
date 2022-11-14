import unittest
from employee import Employee


class TestEmployeeSalary(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('sampsa', 'leikas', 0)
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 5000)
    def test_give_custom_raise(self):
        self.my_employee.give_raise(20_000)
        self.assertEqual(self.my_employee.salary, 20_000)

unittest.main()