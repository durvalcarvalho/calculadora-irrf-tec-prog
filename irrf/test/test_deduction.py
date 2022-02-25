import unittest

from irrf import IRRF


class TestDeduction(unittest.TestCase):
    def setUp(self):
        self.irrf = IRRF()

    def test_register_official_pension(self):
        self.irrf.register_official_pension("Contribuicao compulsoria", 1000.0)
        self.assertEqual(self.irrf.get_total_official_pension(), 1000.0)