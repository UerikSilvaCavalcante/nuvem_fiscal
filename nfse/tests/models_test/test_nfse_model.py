import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from nfse.models import NFSe, Toma
from nfse.enums.nfse_enums import AMBIENTE, PROVEDOR
from pydantic import ValidationError


def test_nfse_model_completo():
    nfse = {
        "provedor": PROVEDOR.PRADAO,
        "ambiente": AMBIENTE.PROD,
        "referencia": "Teste",
    }
    nfse = NFSe(**nfse)
    nfse_serializer = nfse.model_dump()
    esperado = {
        "provedor": PROVEDOR.PRADAO,
        "ambiente": AMBIENTE.PROD,
        "referencia": "Teste",
    }
    assert nfse_serializer == esperado


def test_nfse_model_incompleto():
    nfse = {
        "provedor": PROVEDOR.PRADAO,
        "ambiente": AMBIENTE.PROD,
    }
    nfse = NFSe(**nfse)
    nfse_serializer = nfse.model_dump()
    esperado = {
        "provedor": PROVEDOR.PRADAO,
        "ambiente": AMBIENTE.PROD,
        "referencia": None,
    }
    assert nfse_serializer != esperado


def test_nfse_model_inteiro():
    nfse = 123

    with pytest.raises(TypeError):
        nfse = NFSe(**nfse)  # type: ignore


def test_nfse_model_string():
    nfse = "teste"

    with pytest.raises(TypeError):
        nfse = NFSe(**nfse)  # type: ignore


def test_nfse_model_vazio():
    nfse = {}

    with pytest.raises(ValidationError):
        nfse = NFSe(**nfse)
