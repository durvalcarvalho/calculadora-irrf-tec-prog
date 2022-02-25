

class ValorRendimentoInvalidoException(Exception):
    """
    Exception raised when the income is not a positive numeric value.
    """

class DescricaoEmBrancoException(Exception):
    """
    Exception raised when a deduction description is empty
    """

class ValorDeducaoInvalidoException(Exception):
    """
    Exception raised when a deduction valid is not a positive number.
    """

class NomeEmBrancoException(Exception):
    """
    Exception raised when a dependent name is empty
    """