from empresa.service.serializers.serializer_base import PayloadSerializer


class ConfigNFSeSerializer(PayloadSerializer):
    def __init__(self, config_nfse):
        self._config_nfse = config_nfse

    def serialize(self):
        payload = {
            "regTrib": {
                "opSimpNac": self._config_nfse.opSimpNac,
                "regApTribSN": self._config_nfse.regApTribSN,
                "regEspTrib": self._config_nfse.regEspTrib,
            },
            "rps": {
                "lote": self._config_nfse.lote,
                "serie": self._config_nfse.serie,
                "numero": self._config_nfse.numero,
            },
            "prefeitura": {
                "login": self._config_nfse.login,
                "senha": self._config_nfse.senha,
                "token": self._config_nfse.token,
            },
            "incetivo_fiscal": self._config_nfse.incentivo_fical,
            "ambiente": self._config_nfse.ambiente,
        }
        return payload
