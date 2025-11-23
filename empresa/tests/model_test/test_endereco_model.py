import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from empresa.models import Endereco
from pydantic import ValidationError
from datetime import date


@pytest.mark.parametrize(
    "endereco, esperado",
    [
        (
            {
                "logradouro": "Teste",
                "numero": "123",
                "complemento": "Teste",
                "bairro": "Teste",
                "cidade": "Teste",
                "cep": {"value": "12345678"},
                "pais": "Brasil",
                "uf": "SP",
                "codigo_pais": "1058",
            },
            {
                "logradouro": "Teste",
                "numero": "123",
                "complemento": "Teste",
                "bairro": "Teste",
                "cidade": "Teste",
                "uf": "SP",
                "pais": "Brasil",
                "codigo_pais": "1058",
                "cep": {"value": "12345678"},
            },
        ),
        (
            {
                "logradouro": "Teste",
                "numero": "123",
                "bairro": "Teste",
                "uf": "SP",
                "codigo_pais": "1058",
                "cep": {"value": "12345678"},
            },
            {
                "logradouro": "Teste",
                "numero": "123",
                "complemento": "",
                "bairro": "Teste",
                "cidade": "",
                "cep": "12345678",
                "uf": "SP",
                "pais": "Brasil",
                "codigo_pais": "1058",
                "cep": {"value": "12345678"},
            },
        ),
    ],
)
def test_endereco_model(endereco, esperado):
    endereco = Endereco(**endereco)
    assert endereco.dict() == esperado


@pytest.mark.parametrize("entrada", [123, "test", [], {}])
def test_endereco_model_invalido(entrada):
    with pytest.raises((ValidationError, TypeError)):
        Endereco(**entrada)
