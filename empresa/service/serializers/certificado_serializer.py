from empresa.service.serializers.serializer_base import PayloadSerializer
import base64


class CertificadoSerializer(PayloadSerializer):
    def __init__(self, certificado):
        self._certificado = certificado

    def serialize(self):
        payload = {
            "certificado": base64.b64encode(
                self._certificado.certificado.read()
            ).decode("utf-8"),
            "password": self._certificado.password,
        }
        return payload
