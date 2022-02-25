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
        [[ 
            ("Previdencia oficial", ("Contribuicao compulsoria", 100.0)),
            ("Previdencia oficial", ("Carne INSS", 80.0)),
            ("Dependende", (["Lucas", "Herick"])),
            ("Pensão alimenticia", ([150.0, 200.0])),
            ("Outras deducoes", ("Previdencia privada", 200.0)),
            ("Outras deducoes", ("Funpresp", 50.0)),
        ], 1159.18 ],

        [[
            ("Previdencia oficial", ("Carne INSS", 500.0)),
            ("Dependende", (["Durval", "Leo", "Hugo"])),
            ("Pensão alimenticia", ([300.0])),
            ("Outras deducoes", ("Carne-leao", 200.0)),
        ], 1568.77],
    ])
    def test_get_all_deductions(self, deductions_list, expected_deduction):
        for deduction in deductions_list:
            self.irrf.register_deduction(deduction)
            
        self.assertAlmostEqual(self.irrf.all_deductions, expected_deduction, delta=0.01)
    
    @parameterized.expand([
        [
            [
                Income(value=4125.00, description='Sálario'),
                Income(value=1023.54, description='Ações'),
            ],
            [
                ("Previdencia oficial", ("Contribuicao compulsoria", 400.0)),
                ("Dependende", (["Durval", "Leo", "Hugo"]))
            ], 
            4179.77
        ],
        
        [
            [
                Income(value=3000.00, description='Sálario'),
                Income(value=520.00, description='Ações'),
                Income(value=750.00, description='Alguel recebido'),
            ],
            [
                ("Outras deducoes", ("Previdencia privada", 400.0)),
                ("Pensão alimenticia", ([400.0, 400.0])),
            ], 
            3070.00
        ]
    ])   
    def test_get_calculation_basis(self, income_list, deduction_list, expected_result):
        income: Income
        for income in income_list:
            self.irrf.register_income(income.value, income.description)
            
        for deduction in deduction_list: 
            self.irrf.register_deduction(deduction)
        
        self.assertEqual(self.irrf.calculation_basis, expected_result)

    @parameterized.expand([
        # test case 1
        [ [ Income(value=1000.00, description='Weekly salary') ], [ ], 0.0, ],

        # test case 2
        [ [ Income(value=1903.98, description='Weekly salary') ], [ ], 0.0, ],

        # test case 3 -> **
        [ [ Income(value=1904.12, description='Weekly salary') ], [ ], 0.0, ],

        # test case 4
        [ 
            [ Income(value=2500.00, description='Weekly salary'), ], 
            [ ("Dependende", (["Joao"])) ], 
            30.48,
        ],

        # test case 5
        [ 
            [ Income(value=2826.65, description='Weekly salary'), ],
            [ ("Previdencia oficial", ("Contribuicao compulsoria", 950.0)) ],
            0.0, 
        ],

        # test case 6
        [ 
            [ Income(value=3000.00, description='Weekly salary'), ],
            [ ("Dependende", (["Pedro"])), ("Pensão alimenticia", ([400.0])) ],
            37.98, 
        ],

        # test case 7
        [ 
            [ Income(value=3000.00, description='Weekly salary'), Income(value=500.00, description='Ações')],
            [ ],
            170.20
        ],

        # test case 8
        [ 
            [ Income(value=3750.00, description='Weekly salary'), ],
            [ ("Previdencia oficial", ("Carne INSS", 500.0)), ("Outras deducoes", ("Previdencia privada", 400.0)) ],
            72.70, 
        ],

        # test case 9
        [ [ Income(value=3751.05, description='Weekly salary'), ], [ ], 207.86, ],

        # test case 10
        [ [ Income(value=3751.09, description='Weekly salary'), ], [ ], 207.86, ],

        # test case 11
        [ 
            [ Income(value=4000.00, description='Weekly salary'), ],
            [  ("Dependende", (["Pedro", "Joao"])) ],
            188.32,
        ],

        # test case 12
        [ 
            [ Income(value=4500.00, description='Weekly salary'), ],
            [ ("Pensão alimenticia", ([600.0, 350.0])) ],
            177.70, 
        ],

        # test case 13
        [ 
            [ Income(value=4500.00, description='Weekly salary'), ], 
            [ ("Outras deducoes", ("Previdencia privada", 500.0)) ], 
            263.87, 
        ],

        # test case 14
        [ [ Income(value=4664.68, description='Weekly salary'), ], [ ], 413.42, ],

        # test case 15
        [ [ Income(value=4664.69, description='Weekly salary'), ], [ ], 413.42, ],

        # test case 16
        [ 
            [ Income(value=5000.00, description='Weekly salary'), ],
            [ ("Previdencia oficial", ("Carne INSS", 500.0)), ("Dependende", (["Pedro", "Joao"])) ],
            291.05, 
        ],

        # test case 17
        [ 
            [ Income(value=6000.00, description='Weekly salary'), ],
            [ ("Outras deducoes", ("Previdencia privada", 850.0)), ("Pensão alimenticia", ([600.0, 200.0])) ],
            342.62,
        ],

        # test case 18
        [ [ Income(value=7000.00, description='Weekly salary'), ], [ ], 1055.64, ],

        # test case 19
        [ 
            [ Income(value=8000.00, description='Weekly salary'), ],
            [ ("Dependende", (["Maria", "Joao", "Vinicius", "Fernanda"])) ],
            1122.09, 
        ],

        # test case 20
        [ [ Income(value=9000.00, description='Weekly salary'), ], [ ], 1605.64, ],
    ])
    def test_tax_calculation(self, income_list: Tuple[Income], deduction_list, expected_tax: float):
        income: Income
        for income in income_list:
            self.irrf.register_income(income.value, income.description)
            
        for deduction in deduction_list:
            self.irrf.register_deduction(deduction)

        self.assertAlmostEqual(self.irrf.calculate_tax(), expected_tax, delta=0.01)


    @parameterized.expand([
        [[
            BaseRange(min=0,       max=1903.98,      tax=0.0),
            BaseRange(min=1903.99, max=2826.65,      tax=7.5),
            BaseRange(min=2826.66, max=3751.05,      tax=15.0),
            BaseRange(min=3751.06, max=4664.68,      tax=22.5),
            BaseRange(min=4664.69, max=float('inf'), tax=27.5),
        ], 2022],

        [[
            BaseRange(min=0,       max=1787.77,      tax=0.0),
            BaseRange(min=1787.77, max=2679.29,      tax=7.5),
            BaseRange(min=2679.30, max=3572.43,      tax=15.0),
            BaseRange(min=3572.44, max=4463.81,      tax=22.5),
            BaseRange(min=4463.82, max=float('inf'), tax=27.5),
        ], 2014],

    ])
    def test_registration_of_the_calculation_base_range(self, base_range_table: Tuple[BaseRange], year: int):
        self.irrf.register_calculation_base_range(year=year, table=base_range_table)

        self.assertEqual(
            self.irrf.get_calculation_base_range(year=year),
            base_range_table,
        )

    @parameterized.expand([
        # test case 1
        [ [ Income(value=1000.00, description='Weekly salary'), ], 0.0, ],

        # test case 2
        [ [ Income(value=1903.98, description='Weekly salary'), ], 0.0, ],

        # test case 3 -> **
        [ [ Income(value=1904.12, description='Weekly salary'), ], 0.0, ],

        # test case 4
        [ [ Income(value=2500.00, description='Weekly salary'), ], 1.78, ],

        # test case 5
        [ [ Income(value=2826.65, description='Weekly salary'), ], 2.44, ],

        # test case 6
        [ [ Income(value=3000.00, description='Weekly salary'), ], 3.17, ],

        # test case 7
        [ [ Income(value=3500.00, description='Weekly salary'), ], 4.86, ],

        # test case 8
        [ [ Income(value=3750.00, description='Weekly salary'), ], 5.53, ],

        # test case 9
        [ [ Income(value=3751.05, description='Weekly salary'), ], 5.54, ],

        # test case 10
        [ [ Income(value=3751.09, description='Weekly salary'), ], 5.54, ],

        # test case 11
        [ [ Income(value=4751.09, description='Weekly salary'), ], 9.20, ],

        # test case 12
        [ [ Income(value=4832.17, description='Weekly salary'), ], 9.50, ],

        # test case 13
        [ [ Income(value=8432.17, description='Weekly salary'), ], 17.18, ],

        # test case 14
        [ [ Income(value=18432.17, description='Weekly salary'), ], 22.78, ],

        # test case 15
        [ [ Income(value=81432.17, description='Weekly salary'), ], 26.43, ],

        # test case 16
        [ [ Income(value=200000.00, description='Weekly salary'), ], 27.06, ],
    ])
    def test_effective_rate(self, income_list: Tuple[Income], expected_rate: float):
        income: Income
        for income in income_list:
            self.irrf.register_income(income.value, income.description)

        self.assertAlmostEqual(self.irrf.effective_rate, expected_rate, delta=0.02)
