import unittest

from irrf import IRRF


class TestDeduction(unittest.TestCase):
    def setUp(self):
        self.irrf = IRRF()

    def test_register_official_pension(self):
        self.irrf.register_official_pension("Contribuicao compulsoria", 1000.0)
        self.assertEqual(self.irrf.get_total_official_pension(), 1000.0)

    def test_another_register_official_pension(self):
        self.irrf.register_official_pension("Contribuicao compulsoria", 800.0)
        self.assertEqual(self.irrf.get_total_official_pension(), 800.0)

    def test_multiple_register_official_pension(self):
        self.irrf.register_official_pension("Contribuicao compulsoria", 800.0)
        self.irrf.register_official_pension("Carne Inss", 1000.0)
        self.irrf.register_official_pension("Carne Inss 2", 200.0)
        self.assertEqual(self.irrf.get_total_official_pension(), 2000.0)