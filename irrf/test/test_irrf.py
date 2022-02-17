from typing import Tuple
import unittest
from parameterized import parameterized

from irrf import IRRF, Income


class IRRFTestCase(unittest.TestCase):

    def setUp(self):
        self.irrf = IRRF()

    @parameterized.expand([
        [ Income(value=1000, description='Weekly salary'), ],
        [ Income(value=300, description='Interest on equity'), ],
        [ Income(value=1500, description='Rent income'),  ],
    ])
    def test_register_income_1(self, income: Income):
        self.irrf.register_income(
            value=income.value,
            description=income.description,
        )
        self.assertEqual(self.irrf.total_income, income.value)

    @parameterized.expand([
        [[
            Income(value=1000, description='Weekly salary'),
            Income(value=300, description='Interest on equity'),
            Income(value=1500, description='Rent income'),
        ]],

        [[
            Income(value=1750, description='Weekly salary'),
            Income(value=13000, description='Car sale'),
            Income(value=20000, description='Property sale'),
        ]],
    ])
    def test_register_income_with_multiple_incomes(self, income_list: Tuple[Income], *args, **kwargs):

        total_income = 0

        income: Income
        for income in income_list:
            total_income += income.value

            self.irrf.register_income(
                value=income.value,
                description=income.description,
            )

        self.assertEqual(self.irrf.total_income, total_income)