from typing import Tuple
import unittest
from parameterized import parameterized

from irrf import IRRF, Income, BaseRange


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

    @parameterized.expand([
        [[
            Income(value=1000, description='Weekly salary'),
            Income(value=300, description='Interest on equity'),
            Income(value=1500, description='Rent income'),
        ]],

        [[
            # Testing empty list
        ]],
    ])
    def test_get_all_income_already_declared(self, income_list: Tuple[Income]):
        income: Income
        for income in income_list:
            self.irrf.register_income(income.value, income.description)

        # Here I convert to a list to be able to compare the values,
        # regardless of the data type
        self.assertEqual(
            list(self.irrf.declared_incomes),
            list(income_list),
        )

    @parameterized.expand([
        # test case 1
        [ [ Income(value=1000.00, description='Weekly salary'), ], 0.0, ],

        # test case 2
        [ [ Income(value=1903.98, description='Weekly salary'), ], 0.0, ],

        # test case 3
        [ [ Income(value=1904.12, description='Weekly salary'), ], 0.1, ],

        # test case 4
        [ [ Income(value=2500.00, description='Weekly salary'), ], 44.70, ],

        # test case 5
        [ [ Income(value=2826.65, description='Weekly salary'), ], 69.20, ],

        # test case 6
        [ [ Income(value=3000.00, description='Weekly salary'), ], 95.20, ],

        # test case 7
        [ [ Income(value=3500.00, description='Weekly salary'), ], 170.20, ],

        # test case 8
        [ [ Income(value=3750.00, description='Weekly salary'), ], 207.70, ],

        # test case 9
        [ [ Income(value=3751.05, description='Weekly salary'), ], 207.86, ],

        # test case 10
        [ [ Income(value=3751.09, description='Weekly salary'), ], 207.86, ],

        # test case 11
        [ [ Income(value=4000.00, description='Weekly salary'), ], 263.87, ],

        # test case 12
        [ [ Income(value=4500.00, description='Weekly salary'), ], 376.37, ],

        # test case 13
        [ [ Income(value=4500.00, description='Weekly salary'), ], 376.37, ],

        # test case 14
        [ [ Income(value=4664.68, description='Weekly salary'), ], 413.42, ],

        # test case 15
        [ [ Income(value=4664.69, description='Weekly salary'), ], 413.42, ],

        # test case 16
        [ [ Income(value=5000.00, description='Weekly salary'), ], 505.64, ],

        # test case 17
        [ [ Income(value=6000.00, description='Weekly salary'), ], 780.64, ],

        # test case 18
        [ [ Income(value=7000.00, description='Weekly salary'), ], 1055.64, ],

        # test case 19
        [ [ Income(value=8000.00, description='Weekly salary'), ], 1330.64, ],

        # test case 20
        [ [ Income(value=9000.00, description='Weekly salary'), ], 1605.64, ],
    ])
    def test_tax_calculation(self, income_list: Tuple[Income], expected_tax: float):
        income: Income
        for income in income_list:
            self.irrf.register_income(income.value, income.description)

        self.assertEqual(self.irrf.calculate_tax(), expected_tax)


    def test_registration_of_the_calculation_base_range(self):
        table_2022 = [
            BaseRange(min=0,       max=1903.98,      tax=0.0),
            BaseRange(min=1903.99, max=2826.65,      tax=7.5),
            BaseRange(min=2826.66, max=3751.05,      tax=15.0),
            BaseRange(min=3751.06, max=4664.68,      tax=22.5),
            BaseRange(min=4664.69, max=float('inf'), tax=27.5),
        ]

        self.irrf.register_calculation_base_range(year=2022, table=table_2022)

        self.assertEqual(
            self.irrf.get_calculation_base_range(year=2022),
            table_2022,
        )
