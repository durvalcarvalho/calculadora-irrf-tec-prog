import numbers
from exceptions import InvalidIncomeValueError


class Income:
    def __init__(self, value: int, description: str):
        if not isinstance(value, numbers.Number) or value <= 0:
            raise InvalidIncomeValueError(
                f'The income value must be a positive number, got {value}'
            )
        self.value = value
        self.description = description


class IRRF:

    def __init__(self) -> None:
        self.total_income: float = 0

    def register_income(self, value: float, description: str) -> None:
        self.total_income += value
