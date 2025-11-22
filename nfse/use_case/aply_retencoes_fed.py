from nfse.domain.calculators.impostos_strategy import (
    ImpostovCofins,
    ImpostovPis,
    ImpostovRetCSLL,
    ImpostosStrategy,
)
from decimal import Decimal
from typing import List


class AplyRetencoesFederais:
    def execute(self, vServ: Decimal):
        vPis = ImpostovPis(vServ)
        vCofins = ImpostovCofins(vServ)
        vRetCSLL = ImpostovRetCSLL(vServ)

        return {
            "CST": "01",
            "vPis": vPis.get_vPis,
            "vCofins": vCofins.get_vCofins,
            "vRetCSLL": vRetCSLL.get_vRetCSLL,
            "tpRetPisCofins": 1,
        }
