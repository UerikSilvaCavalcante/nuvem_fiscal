from service.serializers.serializer_base import PayloadSerializer
from empresa.models import Empresa, Endereco
from empresa.service.serializers.endereco_serializer import EnderecoSerializer


class EmpresaSerializer(PayloadSerializer):
    def __init__(self, empresa: Empresa, endereco: Endereco) -> None:
        self._empresa = empresa
        self._endereco = endereco

    def serialize(self) -> dict:
        self._endereco_serializer = EnderecoSerializer(self._endereco).serialize()
        payload = {
            "cpf_cpnj": self._empresa.cpf_cnpj,
            "razao_social": self._empresa.nome_razao_social,
            "inscricao_estadual": self._empresa.inscricao_estadual,
            "inscricao_municipal": self._empresa.inscricao_municipal,
            "nome_fantasia": self._empresa.nome_fantasia,
            "fone": self._empresa.fone,
            "email": self._empresa.email,
            "endereco": self._endereco_serializer,
        }
        return payload
