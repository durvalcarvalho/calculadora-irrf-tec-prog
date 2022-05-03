from unicodedata import name
import unittest

from irrf import IRRF
from income import Incomes
from deduction import Deduction, Deductions

from parameterized import parameterized
from exceptions import DescricaoEmBrancoException, ValorDeducaoInvalidoException


class TestDeduction(unittest.TestCase):
    def setUp(self):
        self.irrf = IRRF(Incomes(), Deductions())

    @parameterized.expand([
        ('Contribuicao compulsoria', 1000.0),
        ('Carne INSS', 800.0),
        ('Carne INSS 2', 200.0)
    ])
    def test_register_official_pension(self, description, value):
        deduction_tuple = (description, value)
        self.irrf._deductions.register_official_pension(deduction_tuple)
        self.assertEqual(self.irrf._deductions.get_total_official_pension(), value)

    @parameterized.expand([
        ('', 100.0),
        ('', 300.0),
        ('', 400.0),
    ])
    def test_blank_name_register_official_pension(self, description, value):
        with self.assertRaises(DescricaoEmBrancoException):
            Deduction('Previdencia oficial', description=description, value=value)

    @parameterized.expand([
        ('Contribuicao compulsoria', -100.0),
        ('Carne INSS', -300.0),
        ('Carne INSS 2', -400.0),
    ])
    def test_blank_name_register_official_pension(self, description, value):
        with self.assertRaises(ValorDeducaoInvalidoException):
            Deduction('Previdencia oficial', description=description, value=value)


    @parameterized.expand([
        (['Guilherme'], 189.59),
        (['Guilherme', 'Felipe'], 189.59*2),
        (['Guilherme', 'Felipe', 'Barbara'], 189.59*3),
    ])
    def test_register_dependent(self, names, value):
        for name in names:
            self.irrf._deductions.register_dependent(name)
        self.assertEqual(self.irrf._deductions.get_total_dependent_deductions(), value)

    @parameterized.expand([
        (['']),
    ])
    def test_blank_name_dependent(self, names):
        for name in names:
            with self.assertRaises(ValorDeducaoInvalidoException):
                Deduction('Dependente', description='Dependente', value=189.59, name=name)

    @parameterized.expand([
        ([1500.0], 1500.0),
        ([1500.0, 300.0], 1800.0),
        ([1500.0, 300.0, 200.0], 2000.0),
    ])
    def test_register_food_pension(self, values, expect):
        for value in values:
            self.irrf._deductions.register_food_pension(value)
        
        self.assertEqual(self.irrf._deductions.get_total_food_pension(), expect)


    @parameterized.expand([
        ([('Previdencia privada', 500.0)], 500.0),
        ([
            ('Previdencia privada', 500.0),
            ('Funpresp', 500.0)
        ], 1000.0),
        ([
            ('Previdencia privada', 500.0),
            ('Funpresp', 500.0),
            ('Carne-leao', 300.0)
        ], 1300.0),
    ])
    def test_other_deductions(self, objects, expect):
        for object in objects:
            self.irrf._deductions.register_other_deductions(object)

        self.assertEqual(self.irrf._deductions.get_other_deductions(), expect)

