import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from nfse.models import Serv
from nfse.enums.dados_fiscais_enums import CNAONIFENUM
from pydantic import ValidationError


@pytest.mark.parametrize(
    "serv, esperado",
    [
        (
            {
                "cLocPrestacao": "Teste",
                "cPaisPrestacao": "1058",
                "cServ": {
                    "cTribNac": "123456",
                    "cTribMun": "123456",
                    "CNAE": "123456",
                    "xDescServ": "Teste",
                    "cNBS": "123456",
                },
            },
            {
                "cLocPrestacao": "Teste",
                "cPaisPrestacao": "1058",
                "cServ": {
                    "cTribNac": "123456",
                    "cTribMun": "123456",
                    "CNAE": "123456",
                    "xDescServ": "Teste",
                    "cNBS": "123456",
                },
            },
        ),
        (
            {
                "cServ": {
                    "cTribNac": "123456",
                    "xDescServ": "Teste",
                },
            },
            {
                "cLocPrestacao": None,
                "cPaisPrestacao": "1058",
                "cServ": {
                    "cTribNac": "123456",
                    "cTribMun": "",
                    "CNAE": "",
                    "xDescServ": "Teste",
                    "cNBS": "",
                },
            },
        ),
    ],
)
def test_serv_model(serv, esperado):
    serv = Serv(**serv)
    serv_serializer = serv.model_dump()
    assert serv_serializer == esperado


@pytest.mark.parametrize("entrada", [1123, "teste", [], {}])
def test_serv_model_invalido(entrada):
    with pytest.raises((ValidationError, TypeError)):
        serv = Serv(**entrada)
