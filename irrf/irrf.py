"""
Módulo que implementa as classes:
* `BaseRange`: Dataclass que agrupa os valores de um intervalo de base.
* `IRRF`: Classe agrupa as rotinas necessárias para calcular o IRRF.
* `Tax`: Classe que abstrai o cálculo do IRRF.
"""

import numbers

from deduction import Deductions
from income import Incomes

from typing import Dict, List

from functools import total_ordering

from const import ZERO

@total_ordering
class BaseRange:
    """
    Dataclasse que abstrai um intervalo de base.
    """
    def __init__(self, min: int, max: int, tax: float):
        self.min = min
        self.max = max
        self.tax = tax

    def __eq__(self, other):
        return(
            round(self.min, 2) == round(other.min, 2) and
            round(self.max, 2) == round(other.max, 2) and
            round(self.tax, 2) == round(other.tax, 2)
        )

    def __lt__(self, other):
        return round(self.min, 2) < round(other.min, 2)

class IRRF:
    """
    Classe que agrupa as rotinas necessárias para calcular o IRRF.
    """

    def __init__(self, incomes: Incomes, deductions: Deductions) -> None:
        self._incomes = incomes
        self._deductions = deductions
        self._calculation_base_ranges: Dict[int, List[BaseRange]] = {}

    def get_tax(self):
        return Tax(self).compute()

    def register_calculation_base_range(
        self,
        year: int,
        table: List[BaseRange],
    ) -> None:
        self._calculation_base_ranges[year] = table

    def get_calculation_base_range(self, year: int) -> List[BaseRange]:
        return self._calculation_base_ranges[year]

    @property
    def calculation_basis(self):
        return self._incomes.total_income - self._deductions.all_deductions

    @property
    def effective_rate(self) -> float:
        tax = self.get_tax()
        effective_rate = (tax / self._incomes.total_income) * 100
        return round(effective_rate, 2)

class Tax:
    """
    Classe que agrupa as rotinas necessárias para
    calcular o imposto nas várias faixas de base.
    """

    TAX_EXEMPT_VALUE = 1903.99
    FIRST_TAX_STEP = 2826.66
    SECOND_TAX_STEP = 3751.06
    THIRD_TAX_STEP = 4664.69

    FIRST_ALIQUOT = 7.5 / 100
    SECOND_ALIQUOT = 15 / 100
    THIRD_ALIQUOT = 22.5 / 100
    FOURTH_ALIQUOT = 27.5 / 100

    EXEMPT_VALUE = 142.80
    FIRST_RANGE_EXEMPT_VALUE = 354.80
    SECOND_RANGE_EXEMPT_VALUE = 636.13
    THIRD_RANGE_EXEMPT_VALUE = 869.36

    def __init__(self, irrf: IRRF) -> None:
        self._irrf = irrf
        self.tax = 0.0

    def is_within_range(self, lower: float, upper: float) -> bool:
        """
        Verifica se o valor está dentro ou não de uma determinada faixa.
        """
        lower_bound = lower
        upper_bound = upper
        return lower_bound <= self._irrf.calculation_basis < upper_bound

    def calculate_tax(self, aliquot: float, exempt_value: float) -> float:
        """
        Calcula o imposto de renda a partir da faixa definida
        """
        return self._irrf.calculation_basis * aliquot - exempt_value

    def compute(self):
        """
        Computa o imposto de acordo com a faixa base
        """
        aliquot = ZERO
        exempt_value = ZERO

        if self._irrf.calculation_basis < Tax.TAX_EXEMPT_VALUE:
            self.tax = 0

        elif self.is_within_range(
            Tax.TAX_EXEMPT_VALUE,
            Tax.FIRST_TAX_STEP):
            aliquot = Tax.FIRST_ALIQUOT
            exempt_value = Tax.EXEMPT_VALUE

        elif self.is_within_range(
            Tax.FIRST_TAX_STEP,
            Tax.SECOND_TAX_STEP):
            aliquot = Tax.SECOND_ALIQUOT
            exempt_value = Tax.FIRST_RANGE_EXEMPT_VALUE

        elif self.is_within_range(
            Tax.SECOND_TAX_STEP,
            Tax.THIRD_TAX_STEP):
            aliquot = Tax.THIRD_ALIQUOT
            exempt_value = Tax.SECOND_RANGE_EXEMPT_VALUE

        else:
            aliquot = Tax.FOURTH_ALIQUOT
            exempt_value = Tax.THIRD_RANGE_EXEMPT_VALUE

        self.tax = self.calculate_tax(aliquot, exempt_value)

        return round(self.tax, 2)
