import unittest

from irrf import IRRF, Deduction
from parameterized import parameterized
from exceptions import DescricaoEmBrancoException, ValorDeducaoInvalidoException


class TestDeduction(unittest.TestCase):
    def setUp(self):
        self.irrf = IRRF()

    @parameterized.expand([
        ('Contribuicao compulsoria', 1000.0),
        ('Carne INSS', 800.0),
        ('Carne INSS 2', 200.0)
    ])
    def test_register_official_pension(self, description, value):
        self.irrf.register_official_pension(description, value)
        self.assertEqual(self.irrf.get_total_official_pension(), value)

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

    def test_register_dependent(self):
        self.irrf.register_dependent('Guilherme')
        self.assertEqual(self.irrf.get_total_dependent_deductions(), 189.59)

    def test_register_dependent_2(self):
        self.irrf.register_dependent('Guilherme')
        self.irrf.register_dependent('Felipe')
        self.assertEqual(self.irrf.get_total_dependent_deductions(), (189.59)*2)
