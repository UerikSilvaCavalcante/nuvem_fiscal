import os
import sys
import pytest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
)


from empresa.models import Empresa
from pydantic import ValidationError
from datetime import date


@pytest.mark.parametrize(
    "empresa, esperado",
    [
        (
            {
                "cpf_cnpj": "123456789",
                "nome_razao_social": "Empresa Teste",
                "created_at": date.today(),
                "updated_at": date.today(),
                "inscricao_estadual": "123456789",
                "inscricao_municipal": "123456789",
                "nome_fantasia": "Empresa Teste",
                "fone": "123456789",
                "email": "2OqUH@example.com",
            },
            {
                "cpf_cnpj": "123456789",
                "nome_razao_social": "Empresa Teste",
                "created_at": date.today(),
                "updated_at": date.today(),
                "inscricao_estadual": "123456789",
                "inscricao_municipal": "123456789",
                "nome_fantasia": "Empresa Teste",
                "fone": "123456789",
                "email": "2OqUH@example.com",
            },
        ),
        (
            {
                "cpf_cnpj": "123456789",
                "nome_razao_social": "Empresa Teste",
                "email": "2OqUH@example.com",
            },
            {
                "cpf_cnpj": "123456789",
                "nome_razao_social": "Empresa Teste",
                "created_at": date.today(),
                "updated_at": date.today(),
                "inscricao_estadual": "",
                "inscricao_municipal": "",
                "nome_fantasia": "",
                "fone": "",
                "email": "2OqUH@example.com",
            },
        ),
    ],
)
def test_empresa_model(empresa, esperado):
    empresa = Empresa(**empresa)
    empresa_serializer = empresa.model_dump()
    assert empresa_serializer == esperado


@pytest.mark.parametrize("entrada", [123, "test", [], {}, None])
def test_empresa_model_invalido(entrada):
    with pytest.raises((ValidationError, TypeError)):
        Empresa(**entrada)
