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

@total_ordering
class BaseRange:
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

    def __init__(self) -> None:
        self.total_income: float = 0
        self._declared_incomes: List[Income] = []
        self._calculation_base_ranges: Dict[int, List[BaseRange]] = {}

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
            tax = self.total_income * (7.5 / 100) - 142.80

        elif 2826.66 <= self.total_income < 3751.06:
            tax = self.total_income * (15 / 100) - 354.80

        elif 3751.06 <= self.total_income < 4664.69:
            tax = self.total_income * (22.5 / 100) - 636.13

        else:
            tax = self.total_income * (27.5 / 100) - 869.36

        return round(tax, 2)

    def register_calculation_base_range(self, year: int, table: List[BaseRange]) -> None:
        self._calculation_base_ranges[year] = table

    def get_calculation_base_range(self, year: int) -> List[BaseRange]:
        return self._calculation_base_ranges[year]
