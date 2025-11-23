from service.serializers.serializer_base import PayloadSerializer
from nfse.models import Cancelamento


class CancelarNFSeSerializer(PayloadSerializer):
    def __init__(self, cancelamento: Cancelamento):
        self._cancelamento = cancelamento

    def serialize(self):
        payload = {
            "codigo": self._cancelamento.codigo,
            "motivo": self._cancelamento.motivo,
        }
        return payload
