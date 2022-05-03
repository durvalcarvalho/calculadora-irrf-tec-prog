"""
Módulo que implementa as classes:
* `Income`: Dataclass que agrupa os dados de um recebimento.
* `Incomes`: Classe agrupa as rotinas necessárias para calcular a renda.
"""

import numbers

from deduction import Deductions

from exceptions import (
    DescricaoEmBrancoException,
    ValorRendimentoInvalidoException,
)

from typing import List

from functools import total_ordering

from const import ZERO, VALUE_EXCEPTION_TEXT, NULL_EXCEPTION_TEXT

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

class Incomes:
    """
    Classe que agrupa as rotinas necessárias para
    calcular o imposto nas várias faixas de base.
    """

    def __init__(self) -> None:
        self._declared_incomes: List[Income] = []

        self.total_income: float = ZERO

    def register_income(self, value: float, description: str) -> None:
        self.total_income += value

        self._declared_incomes.append(
            Income(value=value, description=description),
        )
    
    @property
    def declared_incomes(self) -> List[Income]:
        return self._declared_incomes

    @declared_incomes.setter
    def declared_incomes(self, value: List[Income]) -> None:
        raise RuntimeError(
            "It is not allowed to change the list of declared income"
        )