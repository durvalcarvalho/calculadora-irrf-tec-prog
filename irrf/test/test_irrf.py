from collections import namedtuple
import unittest
from parameterized import parameterized

from irrf import IRRF


class IRRFTestCase(unittest.TestCase):

    Income = namedtuple('Income', ['value', 'description'])

    def setUp(self):
        self.irrf = IRRF()

    @parameterized.expand([
        ( Income(value=1000, description='Weekly salary'), ),
        ( Income(value=300, description='Interest on equity'), ),
        ( Income(value=1500, description='Rent income'),  ),
    ])
    def test_register_income_1(self, income: Income, *args, **kwargs):
        self.irrf.register_income(
            value=income.value,
            description=income.description,
        )
        self.assertEqual(self.irrf.total_income, income.value)

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