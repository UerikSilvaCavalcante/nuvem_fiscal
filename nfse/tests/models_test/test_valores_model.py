import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from nfse.models import Valores
from nfse.enums.tribmun_enums import TRIBISSQN, TPRETISSQN, TPIMUNIDADE
from nfse.enums.piscofins_enum import CST, TPRETPISCOFINS
from pydantic import ValidationError
from decimal import Decimal


@pytest.mark.parametrize(
    "valores, esperado",
    [
        (
            {
                "vServPreset": {
                    "vReceb": Decimal(10.00),
                    "vServ": Decimal(10.00),
                },
                "vDescCondIncond": {
                    "vDescIncond": Decimal(10.00),
                    "vDescCond": Decimal(10.00),
                },
                "trib": {
                    "tribMun": {
                        "tribISSQN": TRIBISSQN.OP_TRIBUTAVEL,
                        "cLocIncid": "local Teste",
                        "cPaisResult": "1058",
                        "tpImunidade": TPIMUNIDADE.LIVROS,
                        "pAliq": Decimal(10.00),
                        "tpRetISSQN": TPRETISSQN.N_RETIDNO,
                    },
                    "tribFed": {
                        "piscofins": {
                            "CST": CST.TRIBUTADO_BASICO,
                            "vPis": Decimal(10.00),
                            "vCofins": Decimal(10.00),
                            "vRetCSLL": Decimal(10.00),
                            "tpRetPisCofins": TPRETPISCOFINS.NAO_RETIDO,
                        },
                        "vRetCSLL": Decimal(10.00),
                    },
                    "totTrib": {
                        "vTotTrib": {
                            "vTotTribFed": Decimal(10.00),
                            "vTotTribMun": Decimal(10.00),
                            "vTotTribEst": Decimal(10.00),
                        },
                        "pTotTrib": {
                            "pTotTribFed": Decimal(10.00),
                            "pTotTribMun": Decimal(10.00),
                            "pTotTribEst": Decimal(10.00),
                        },
                        "indTotTrib": 1,
                        "pTotTribSN": Decimal(10.00),
                    },
                },
            },
            {
                "vServPreset": {
                    "vReceb": Decimal(10.00),
                    "vServ": Decimal(10.00),
                },
                "vDescCondIncond": {
                    "vDescIncond": Decimal(10.00),
                    "vDescCond": Decimal(10.00),
                },
                "trib": {
                    "tribMun": {
                        "tribISSQN": TRIBISSQN.OP_TRIBUTAVEL,
                        "cLocIncid": "local Teste",
                        "cPaisResult": "1058",
                        "tpImunidade": TPIMUNIDADE.LIVROS,
                        "pAliq": Decimal(10.00),
                        "tpRetISSQN": TPRETISSQN.N_RETIDNO,
                    },
                    "tribFed": {
                        "piscofins": {
                            "CST": CST.TRIBUTADO_BASICO,
                            "vPis": Decimal(10.00),
                            "vCofins": Decimal(10.00),
                            "tpRetPisCofins": TPRETPISCOFINS.NAO_RETIDO,
                        },
                        "vRetCSLL": Decimal(10.00),
                    },
                    "totTrib": {
                        "vTotTrib": {
                            "vTotTribFed": Decimal(10.00),
                            "vTotTribMun": Decimal(10.00),
                            "vTotTribEst": Decimal(10.00),
                        },
                        "pTotTrib": {
                            "pTotTribFed": Decimal(10.00),
                            "pTotTribMun": Decimal(10.00),
                            "pTotTribEst": Decimal(10.00),
                        },
                        "indTotTrib": 1,
                        "pTotTribSN": Decimal(10.00),
                    },
                },
            },
        ),
        (
            {
                "vServPreset": {
                    "vReceb": Decimal(10.00),
                    "vServ": Decimal(10.00),
                },
                "trib": {
                    "tribMun": {
                        "tribISSQN": TRIBISSQN.OP_TRIBUTAVEL,
                        "cLocIncid": "local Teste",
                        "cPaisResult": "1058",
                        "tpImunidade": TPIMUNIDADE.LIVROS,
                        "pAliq": Decimal(10.00),
                        "tpRetISSQN": TPRETISSQN.N_RETIDNO,
                    }
                },
            },
            {
                "vServPreset": {
                    "vReceb": Decimal(10.00),
                    "vServ": Decimal(10.00),
                },
                "vDescCondIncond": None,
                "trib": {
                    "tribMun": {
                        "tribISSQN": TRIBISSQN.OP_TRIBUTAVEL,
                        "cLocIncid": "local Teste",
                        "cPaisResult": "1058",
                        "tpImunidade": TPIMUNIDADE.LIVROS,
                        "pAliq": Decimal(10.00),
                        "tpRetISSQN": TPRETISSQN.N_RETIDNO,
                    },
                    "tribFed": None,
                    "totTrib": None,
                },
            },
        ),
    ],
)
def test_valores_model(valores, esperado):
    valores = Valores(**valores)
    valores_serializer = valores.model_dump()
    assert valores_serializer == esperado


@pytest.mark.parametrize("entrada", [123, "test", [], {}])
def test_valores_model_inesperado(entrada):
    with pytest.raises((ValidationError, TypeError)):
        Valores(**entrada)
