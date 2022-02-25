import unittest
from irrf import Income
from exceptions import ValorRendimentoInvalidoException, DescricaoEmBrancoException

from parameterized import parameterized


class IncomeTestCase(unittest.TestCase):

    @parameterized.expand([
        (2500, 'Salary'),
        (500, 'Rent'),
        (25, 'Nubank Interest'),
    ])
    def test_income_class_constructor(self, value, description):
        income = Income(value, description)
        self.assertEqual(income.value, value)
        self.assertEqual(income.description, description)


    @parameterized.expand([
        (-2500, 'Salary'),
        (-500, 'Rent'),
        (-25, 'Nubank Interest'),
    ])
    def tests_if_the_constructor_refuses_negative_values(self, value, description):
        with self.assertRaises(ValorRendimentoInvalidoException):
            Income(value, description)

    @parameterized.expand([
        ('-2500', 'Salary'),
        ('Rent', 'Rent'),
        ([1,2,3], 'Nubank Interest'),
        ({1:10, 2:20}, 'Nubank Interest'),
        ({1:10, 2:20}, 'Nubank Interest'),
    ])
    def test_if_constructor_refuses_non_numeric_values(self, value, description):
        with self.assertRaises(ValorRendimentoInvalidoException):
            Income(value, description)
            
    @parameterized.expand([
        (1000.0, ''),
        (10.0, ' '),
        (500.0, '     '),
    ])
    def test_if_constructor_refuses_blank_descriptions(self, value, description):
        with self.assertRaises(DescricaoEmBrancoException):
            Income(value, description)
