import unittest
from parameterized import parameterized

from irrf import IRRF


class IRRFTestCase(unittest.TestCase):

    def setUp(self):
        self.irrf = IRRF()

    def test_register_income_1(self):
        self.irrf.register_income(
            value=1000,
            description='Weekly salary',
        )
        self.assertEqual(self.irrf.total_income, 1000)

    def test_register_income_2(self):
        self.irrf.register_income(
            value=300,
            description='Interest on equity',
        )
        self.assertEqual(self.irrf.total_income, 300)

    def test_register_income_3(self):
        self.irrf.register_income(
            value=1500,
            description='Rent income',
        )
        self.assertEqual(self.irrf.total_income, 1500)

    def test_register_income_with_multiple_incomes(self):
        self.irrf.register_income(
            value=1000,
            description='Weekly salary',
        )
        self.irrf.register_income(
            value=300,
            description='Interest on equity',
        )
        self.irrf.register_income(
            value=1500,
            description='Rent income',
        )
        self.assertEqual(self.irrf.total_income, 2800)