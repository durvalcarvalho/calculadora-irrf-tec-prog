"""
Módulo que implementa as classes:
* `Deduction`: Dataclass que agrupa os dados de uma dedução.
* `Deductions`: Classe agrupa as rotinas necessárias para calcular as deduções.
"""

import numbers

from exceptions import (
    DescricaoEmBrancoException,
    NomeEmBrancoException,
    ValorDeducaoInvalidoException,
)

from typing import List, Tuple

from functools import total_ordering

from const import ZERO, VALUE_EXCEPTION_TEXT, NULL_EXCEPTION_TEXT

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

class Deductions:

    DEPENDENT_DEDUCTION = 189.59

    def __init__(self) -> None:
        self._declared_deductions: List[Deduction] = []

        self._official_pension_total_value = ZERO
        self._dependent_deductions = ZERO
        self._food_pension = ZERO
        self._other_deductions_value = ZERO

    def register_deduction(self, deduction: Tuple[str, Tuple]) -> None:
        deduction_type = deduction[0]
        method = self.select_deduction_method(deduction_type)
        method(deduction[1])

    def select_deduction_method(self, deduction_type):
        possible_methods = {
            "Previdencia oficial": self.register_official_pension,
            "Dependende": self.loop_over_dependents,
            "Pensão alimenticia": self.loop_over_food_pensions,
            "Outras deducoes": self.register_other_deductions
        }
        return possible_methods[deduction_type]
    
    def get_total_official_pension(self) -> float:
        return self._official_pension_total_value

    def get_total_dependent_deductions(self) -> float:
        return self._dependent_deductions

    def get_total_food_pension(self) -> float:
        return self._food_pension

    def get_other_deductions(self) -> float:
        return self._other_deductions_value

    @property
    def all_deductions(self) -> float:
        total_deductions = (
            self._official_pension_total_value +
            self._dependent_deductions +
            self._food_pension +
            self._other_deductions_value
        )

        return total_deductions

    def register_official_pension(self, deduction_tuple: Tuple[str, float]) -> None:
        description = deduction_tuple[0]
        value = deduction_tuple[1]

        new_deduction = Deduction(
            type="Previdencia oficial",
            description=description,
            value=value,
        )

        self._declared_deductions.append(new_deduction)
        self._official_pension_total_value += new_deduction.value
    
    def register_dependent(self, name: str) -> None:
        new_deduction = Deduction(
            type="Dependente",
            description="Dependente",
            value=Deductions.DEPENDENT_DEDUCTION,
            name=name,
        )
        self._declared_deductions.append(new_deduction)
        self._dependent_deductions += Deductions.DEPENDENT_DEDUCTION

    def loop_over_dependents(self, names) -> None:
        for name in names:
            self.register_dependent(name)

    def register_food_pension(self, value: float) -> None:
        new_deduction = Deduction(
            type="Pensão alimenticia",
            description="Pensao alimenticia",
            value=value
        )
        self._declared_deductions.append(new_deduction)
        self._food_pension += new_deduction.value

    def loop_over_food_pensions(self, values) -> None:
        for value in values:
            self.register_food_pension(value)

    def register_other_deductions(
        self,
        deduction_tuple: Tuple[str, float],
    ) -> None:
        new_deduction = Deduction(
            type='Outras deducoes',
            description=deduction_tuple[0],
            value=deduction_tuple[1]
        )
        self._declared_deductions.append(new_deduction)
        self._other_deductions_value += new_deduction.value
