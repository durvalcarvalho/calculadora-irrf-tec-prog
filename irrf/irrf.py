
class Income:
    def __init__(self, value: int, description: str):
        self.value = value
        self.description = description

class IRRF:

    def __init__(self) -> None:
        self.total_income: float = 0

    def register_income(self, value: float, description: str) -> None:
        self.total_income += value
