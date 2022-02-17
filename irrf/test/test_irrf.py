import unittest
from parameterized import parameterized

from irrf import IRRF


class IRRFTestCase(unittest.TestCase):

    def setUp(self):
        self.irrf = IRRF()

    def test_register_income(self):
        self.irrf.register_income(
            value=1000,
            description='Weekly salary',
        )
        self.assertEqual(self.irrf.total_income, 1000)
