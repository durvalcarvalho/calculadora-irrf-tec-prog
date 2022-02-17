import numbers
from typing import List
from exceptions import InvalidIncomeValueError
from functools import total_ordering


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
        return 0.0