from nfse.domain.calculators.base_calculator_strategy import CalculatorStrategy
from abc import abstractmethod
from decimal import Decimal


class ImpostosStrategy(CalculatorStrategy):
    @abstractmethod
    def calculate(self):
        pass


class ImpostovRetCSLL(ImpostosStrategy):
    def __init__(self, vServ: Decimal) -> None:
        self._pCSLL: Decimal = Decimal(1)
        self._vServ: Decimal = vServ

    def calculate(self):
        self._vRetCSLL = (self._vServ * self._pCSLL) / 100

    @property
    def get_vRetCSLL(self):
        return self._vRetCSLL


class ImpostovPis(ImpostosStrategy):
    def __init__(self, vServ: Decimal) -> None:
        self._vServ: Decimal = vServ
        self._pPis: Decimal = Decimal(0.65)

    def calculate(self):
        self._vPis = (self._vServ * self._pPis) / 100

    @property
    def get_vPis(self):
        return self._vPis


class ImpostovCofins(ImpostosStrategy):
    def __init__(self, vServ: Decimal) -> None:
        self._vServ: Decimal = vServ
        self._pCofins: Decimal = Decimal(3)

    def calculate(self):
        self._vCofins = (self._vServ * self._pCofins) / 100

    @property
    def get_vCofins(self):
        return self._vCofins
