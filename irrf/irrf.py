import numbers
from typing import Dict, List, Tuple
from exceptions import DescricaoEmBrancoException, ValorRendimentoInvalidoException, NomeEmBrancoException, ValorDeducaoInvalidoException
from functools import total_ordering


@total_ordering
class Income:
    def __init__(self, value: int, description: str):
        if not isinstance(value, numbers.Number) or value <= 0:
            raise ValorRendimentoInvalidoException(
                f'The income value must be a positive number, got {value}'
            )
            
        if not description.strip():
            raise DescricaoEmBrancoException(
                'The income description must be filled'
            )
            
        self.value = value
        self.description = description

    def __eq__(self, other):
        return self.value == other.value and self.description == other.description

    def __lt__(self, other):
        return self.value < other.value

@total_ordering
class Deduction:
    def __init__(self, type: str, description: str, value: float, name: str='') -> None:
        if not isinstance(value, numbers.Number) or value <= 0:
            raise ValorDeducaoInvalidoException(
                f'The deduction value must be a positive number, got {value}'
            )
        
        if len(description) < 1:
            raise DescricaoEmBrancoException('The deduction description must be filled')

        if len(name) < 1 and type == "Dependente":
            raise NomeEmBrancoException('You must prove the dependent name')

        self.type = type
        self.description = description
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.description == other.description

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

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
        self._declared_deductions: List[Deduction] = []
        self._official_pension_total_value = 0.0
        self._dependent_deductions = 0.0
        self._food_pension = 0.0
        self._other_deductions_value = 0.0

    def register_income(self, value: float, description: str) -> None:
        self.total_income += value

        self._declared_incomes.append(
            Income(value=value, description=description),
        )
        
    def register_deduction(self, deduction: Tuple[str, Tuple]) -> None:
        if deduction[0] == "Previdencia oficial":
            self.register_official_pension(deduction[1][0], deduction[1][1])
        elif deduction[0] == "Dependende":
            for name in deduction[1]:
                self.register_dependent(name)
        elif deduction[0] == "Pensão alimenticia":
            for value in deduction[1]:
                self.register_food_pension(value)
        elif deduction[0] == "Outras deducoes":
            self.register_other_deductions(deduction[1][0], deduction[1][1])

    @property
    def declared_incomes(self) -> List[Income]:
        return self._declared_incomes

    @declared_incomes.setter
    def declared_incomes(self, value: List[Income]) -> None:
        raise RuntimeError("It is not allowed to change the list of declared income")

    def calculate_tax(self) -> float:
        if self.calculation_basis < 1903.99:
            return 0

        elif 1903.99 <= self.calculation_basis < 2826.66:
            tax = self.calculation_basis * (7.5 / 100) - 142.80

        elif 2826.66 <= self.calculation_basis < 3751.06:
            tax = self.calculation_basis * (15 / 100) - 354.80

        elif 3751.06 <= self.calculation_basis < 4664.69:
            tax = self.calculation_basis * (22.5 / 100) - 636.13

        else:
            tax = self.calculation_basis * (27.5 / 100) - 869.36

        return round(tax, 2)

    def register_calculation_base_range(self, year: int, table: List[BaseRange]) -> None:
        self._calculation_base_ranges[year] = table

    def get_calculation_base_range(self, year: int) -> List[BaseRange]:
        return self._calculation_base_ranges[year]

    def register_official_pension(self, description: str, value: float) -> None:
        self._declared_deductions.append(Deduction(type="Previdencia oficial", description=description, value=value))
        self._official_pension_total_value += value

    def get_total_official_pension(self) -> float:
        return self._official_pension_total_value

    def register_dependent(self, name: str) -> None:
       self._declared_deductions.append(Deduction(type="Dependente", description="Dependente", value=189.59, name=name))
       self._dependent_deductions += 189.59

    def get_total_dependent_deductions(self) -> float:
        return self._dependent_deductions

    def register_food_pension(self, value: float) -> None:
        self._declared_deductions.append(Deduction(type="Pensão alimenticia", description="Pensao alimenticia", value=value))
        self._food_pension += value

    def get_total_food_pension(self) -> float:
        return self._food_pension

    def register_other_deductions(self, description: str, value: float) -> None:
        self._declared_deductions.append(Deduction(type='Outras deducoes', description=description, value=value))
        self._other_deductions_value += value

    def get_other_deductions(self) -> float:
        return self._other_deductions_value

    @property
    def all_deductions(self) -> float:
        return self._official_pension_total_value + self._dependent_deductions + self._food_pension + self._other_deductions_value
    
    @property
    def calculation_basis(self):
        return 2120.82

    @property
    def effective_rate(self) -> float:
        tax = self.calculate_tax()
        effective_rate = (tax / self.total_income) * 100
        return round(effective_rate, 2)
