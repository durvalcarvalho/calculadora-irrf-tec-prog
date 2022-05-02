"""
Módulo que implementa as classes:
* `Income`: Dataclass que agrupa os dados de um recebimento.
* `Deduction`: Dataclass que agrupa os dados de uma dedução.
* `BaseRange`: Dataclass que agrupa os valores de um intervalo de base.
* `IRRF`: Classe agrupa as rotinas necessárias para calcular o IRRF.
* `CalculateTax`: Classe que abstrai o cálculo do IRRF.
"""

import numbers
from typing import Dict, List, Tuple

from exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException,
    NomeEmBrancoException,
    ValorDeducaoInvalidoException,
)

from functools import total_ordering

ZERO = 0.0

VALUE_EXCEPTION_TEXT = lambda type, value: \
    f'The {type} value must be a positive number, got {value}'
NULL_EXCEPTION_TEXT = lambda type: \
    f'The {type} description must be filled'

@total_ordering
class Income:
    """
    Dataclasse que agrupa os dados de um recebimento.
    """
    def __init__(self, value: int, description: str):
        if not isinstance(value, numbers.Number) or value <= 0:
            raise ValorRendimentoInvalidoException(
                VALUE_EXCEPTION_TEXT('income', value)
            )

        if not description.strip():
            raise DescricaoEmBrancoException(
                NULL_EXCEPTION_TEXT('income')
            )

        self.value = value
        self.description = description

    def __eq__(self, other):
        return (
            self.value == other.value and
            self.description == other.description
        )

    def __lt__(self, other):
        return self.value < other.value


@total_ordering
class Deduction:
    """
    Dataclasse que agrupa os valores de uma dedução.
    """
    def __init__(
        self,
        type: str,
        description: str,
        value: float,
        name: str='',
    ) -> None:
        if not isinstance(value, numbers.Number) or value <= 0:
            raise ValorDeducaoInvalidoException(
                VALUE_EXCEPTION_TEXT('deduction', value)
            )

        if not description:
            raise DescricaoEmBrancoException(
                NULL_EXCEPTION_TEXT('deduction')
            )

        if type == "Dependente" and not name:
            raise NomeEmBrancoException('You must prove the dependent name')

        self.type = type
        self.description = description
        self.value = value

    def __eq__(self, other):
        return (
            self.value == other.value and
            self.description == other.description
        )

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


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

    DEPENDENT_DEDUCTION = 189.59

    def __init__(self) -> None:
        self._declared_incomes: List[Income] = []
        self._calculation_base_ranges: Dict[int, List[BaseRange]] = {}
        self._declared_deductions: List[Deduction] = []

        self.total_income: float = ZERO
        self._official_pension_total_value = ZERO
        self._dependent_deductions = ZERO
        self._food_pension = ZERO
        self._other_deductions_value = ZERO

    def register_income(self, value: float, description: str) -> None:
        self.total_income += value

        self._declared_incomes.append(
            Income(value=value, description=description),
        )

    def register_deduction(self, deduction: Tuple[str, Tuple]) -> None:
        method = self.select_deduction_method(deduction[0])
        method(deduction[1])

    def select_deduction_method(self, deduction_type):
        possible_methods = {
            "Previdencia oficial": self.register_official_pension,
            "Dependende": self.loop_over_dependents,
            "Pensão alimenticia": self.loop_over_food_pensions,
            "Outras deducoes": self.register_other_deductions
        }
        return possible_methods[deduction_type]

    @property
    def declared_incomes(self) -> List[Income]:
        return self._declared_incomes

    @declared_incomes.setter
    def declared_incomes(self, value: List[Income]) -> None:
        raise RuntimeError(
            "It is not allowed to change the list of declared income"
        )

    def get_tax(self):
        return CalculateTax(self).compute()

    def register_calculation_base_range(
        self,
        year: int,
        table: List[BaseRange],
    ) -> None:
        self._calculation_base_ranges[year] = table

    def get_calculation_base_range(self, year: int) -> List[BaseRange]:
        return self._calculation_base_ranges[year]

    def register_official_pension(self, deduction_tuple: Tuple[str, float]) -> None:
        description = deduction_tuple[0]
        value = deduction_tuple[1]
        self._declared_deductions.append(
            Deduction(
                type="Previdencia oficial",
                description=description,
                value=value,
            )
        )
        self._official_pension_total_value += value

    def get_total_official_pension(self) -> float:
        return self._official_pension_total_value

    def loop_over_dependents(self, names) -> None:
        for name in names:
            self.register_dependent(name)

    def register_dependent(self, name: str) -> None:
        deduction = Deduction(
            type="Dependente",
            description="Dependente",
            value=IRRF.DEPENDENT_DEDUCTION,
            name=name,
        )
        self._declared_deductions.append(deduction)
        self._dependent_deductions += IRRF.DEPENDENT_DEDUCTION

    def get_total_dependent_deductions(self) -> float:
        return self._dependent_deductions

    def loop_over_food_pensions(self, values) -> None:
        for value in values:
            self.register_food_pension(value)

    def register_food_pension(self, value: float) -> None:
        deduction = Deduction(
            type="Pensão alimenticia",
            description="Pensao alimenticia",
            value=value
        )
        self._declared_deductions.append(deduction)
        self._food_pension += deduction.value

    def get_total_food_pension(self) -> float:
        return self._food_pension

    def register_other_deductions(
        self,
        deduction_tuple: Tuple[str, float],
    ) -> None:
        deduction = Deduction(
            type='Outras deducoes',
            description=deduction_tuple[0],
            value=deduction_tuple[1]
        )
        self._declared_deductions.append(deduction)
        self._other_deductions_value += deduction.value

    def get_other_deductions(self) -> float:
        return self._other_deductions_value

    @property
    def all_deductions(self) -> float:
        return (
            self._official_pension_total_value +
            self._dependent_deductions +
            self._food_pension +
            self._other_deductions_value
        )

    @property
    def calculation_basis(self):
        return self.total_income - self.all_deductions

    @property
    def effective_rate(self) -> float:
        tax = self.get_tax()
        effective_rate = (tax / self.total_income) * 100
        return round(effective_rate, 2)


class CalculateTax:
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

        if self._irrf.calculation_basis < CalculateTax.TAX_EXEMPT_VALUE:
            self.tax = 0

        elif self.is_within_range(
            CalculateTax.TAX_EXEMPT_VALUE,
            CalculateTax.FIRST_TAX_STEP):
            aliquot = CalculateTax.FIRST_ALIQUOT
            exempt_value = CalculateTax.EXEMPT_VALUE

        elif self.is_within_range(
            CalculateTax.FIRST_TAX_STEP,
            CalculateTax.SECOND_TAX_STEP):
            aliquot = CalculateTax.SECOND_ALIQUOT
            exempt_value = CalculateTax.FIRST_RANGE_EXEMPT_VALUE

        elif self.is_within_range(
            CalculateTax.SECOND_TAX_STEP,
            CalculateTax.THIRD_TAX_STEP):
            aliquot = CalculateTax.THIRD_ALIQUOT
            exempt_value = CalculateTax.SECOND_RANGE_EXEMPT_VALUE

        else:
            aliquot = CalculateTax.FOURTH_ALIQUOT
            exempt_value = CalculateTax.THIRD_RANGE_EXEMPT_VALUE

        self.tax = self.calculate_tax(aliquot, exempt_value)

        return round(self.tax, 2)
