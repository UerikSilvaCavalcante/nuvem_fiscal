import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from nfse.models import Toma
from nfse.enums.dados_fiscais_enums import CNAONIFENUM
from pydantic import ValidationError


@pytest.mark.parametrize(
    "toma ,esperado",
    [
        (
            {
                "identificacao": {
                    "cnpj": {"value": "12345678901234"},
                    "cpf": {"value": "71033323128"},
                    "nif": "",
                    "xNome": "Teste",
                },
                "contato": {
                    "fone": "62981545545",
                    "email": {"address": "teste@xpto.com"},
                },
                "dadosFiscais": {
                    "im": "",
                    "ie": "",
                    "caepf": "",
                    "cNaoNIF": CNAONIFENUM.DISPENSADO,
                },
                "end": {
                    "xLgr": "Teste",
                    "nro": "123",
                    "xCpl": "Teste",
                    "xBairro": "Teste",
                    "cMun": "123",
                    "cep": {"value": "74913190"},
                },
            },
            {
                "identificacao": {
                    "cnpj": {"value": "12345678901234"},
                    "cpf": {"value": "71033323128"},
                    "nif": "",
                    "xNome": "Teste",
                    "orgaoPublico": False,
                },
                "contato": {
                    "fone": "62981545545",
                    "email": {"address": "teste@xpto.com"},
                },
                "dadosFiscais": {
                    "im": "",
                    "ie": "",
                    "caepf": "",
                    "cNaoNIF": CNAONIFENUM.DISPENSADO,
                },
                "end": {
                    "xLgr": "Teste",
                    "nro": "123",
                    "xCpl": "Teste",
                    "xBairro": "Teste",
                    "cMun": "123",
                    "cep": {"value": "74913190"},
                    "endExt": None,
                },
            },
        ),
        (
            {
                "identificacao": {
                    "cnpj": {"value": "12345678901234"},
                    "cpf": {"value": "71033323128"},
                    "nif": "",
                    "xNome": "Teste",
                },
                "contato": {
                    "fone": "62981545545",
                    "email": {"address": "teste@xpto.com"},
                },
                "end": {
                    "xLgr": "Teste",
                    "nro": "123",
                    "xCpl": "Teste",
                    "xBairro": "Teste",
                    "cMun": "123",
                    "cep": {"value": "74913190"},
                },
            },
            {
                "identificacao": {
                    "cnpj": {"value": "12345678901234"},
                    "cpf": {"value": "71033323128"},
                    "nif": "",
                    "xNome": "Teste",
                    "orgaoPublico": False,
                },
                "contato": {
                    "fone": "62981545545",
                    "email": {"address": "teste@xpto.com"},
                },
                "dadosFiscais": None,
                "end": {
                    "xLgr": "Teste",
                    "nro": "123",
                    "xCpl": "Teste",
                    "xBairro": "Teste",
                    "cMun": "123",
                    "cep": {"value": "74913190"},
                    "endExt": None,
                },
            },
        ),
    ],
)
def test_toma_model(toma, esperado):
    toma = Toma(**toma)
    toma_serializer = toma.model_dump()
    assert toma_serializer == esperado


@pytest.mark.parametrize("entrada", [1234, "teste", {}])
def test_toma_model_inesperado(entrada):
    with pytest.raises((ValidationError, TypeError)):
        toma = Toma(**entrada)
