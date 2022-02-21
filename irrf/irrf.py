import numbers
from typing import Dict, List
from exceptions import InvalidIncomeValueError
from functools import total_ordering
from collections import namedtuple


@total_ordering
class Income:
    def __init__(self, value: int, description: str):
        if not isinstance(value, numbers.Number) or value <= 0:
            raise InvalidIncomeValueError(
                f'The income value must be a positive number, got {value}'
            )
        self.value = value
        self.description = description

    def __eq__(self, other):
        return self.value == other.value and self.description == other.description

    def __lt__(self, other):
        return self.value < other.value

BaseRange = namedtuple('CalculationBaseRange', 'min max tax')

class IRRF:

    def __init__(self) -> None:
        self.total_income: float = 0
        self._declared_incomes: List[Income] = []

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
        raise RuntimeError("It is not allowed to change the list of declared income")

    def calculate_tax(self) -> float:
        if self.total_income < 1903.99:
            return 0

        elif 1903.99 <= self.total_income < 2826.66:
            return self.total_income * (7.5 / 100) - 142.80

        elif 2826.66 <= self.total_income < 3751.06:
            return self.total_income * (15 / 100) - 354.80

        elif 3751.06 <= self.total_income < 4664.69:
            return self.total_income * (22.5 / 100) - 636.13

        else:
            return self.total_income * (27.5 / 100) - 869.36

    def register_calculation_base_range(self, year: int, table: List[BaseRange]) -> None:
        ...

    def get_calculation_base_range(self, year: int) -> List[BaseRange]:
        return [
            BaseRange(min=0,       max=1903.98,      tax=0.0),
            BaseRange(min=1903.99, max=2826.65,      tax=7.5),
            BaseRange(min=2826.66, max=3751.05,      tax=15.0),
            BaseRange(min=3751.06, max=4664.68,      tax=22.5),
            BaseRange(min=4664.69, max=float('inf'), tax=27.5),
        ]
