import unittest
from parameterized import parameterized

from irrf import IRRF


class IRRFTestCase(unittest.TestCase):

    def setUp(self):
        self.calculadora = IRRF()
