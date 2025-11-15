from service.serializers.serializer_base import PayloadSerializer

from empresa.models import Endereco


class EnderecoSerializer(PayloadSerializer):
    def __init__(self, endereco: Endereco) -> None:
        self._endereco = endereco

    def serialize(self) -> dict:
        payload = {
            "logradouro": self._endereco.logradouro,
            "numero": self._endereco.numero,
            "complemento": self._endereco.complemento,
            "bairro": self._endereco.bairro,
            "cidade": self._endereco.cidade,
            "cep": self._endereco.cep.get(),
            "pais": self._endereco.pais,
            "uf": self._endereco.uf,
            "codigo_pais": self._endereco.codigo_pais,
        }
        return payload
