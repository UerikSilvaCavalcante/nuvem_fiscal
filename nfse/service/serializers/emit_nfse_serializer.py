from nfse.enums import tribmun_enums
from service.serializers.serializer_base import PayloadSerializer

from nfse.models import (
    NFSe,
    InfDPS,
    Preset,
    RegTrib,
    Toma,
    Serv,
    Valores,
)
from value_objects.endereco import Endereco


class RegTribSerializer(PayloadSerializer):
    def __init__(self, regTrib: RegTrib):
        self.regTrib = regTrib

    def serialize(self) -> dict[str, object]:
        payload = {"regespTrib": self.regTrib.regespTrib}
        return payload  # type: ignore


class PresetSerializer(PayloadSerializer):
    def __init__(self, preset: Preset) -> None:
        self.preset = preset

    def serialize(self) -> dict[str, object]:
        payload = {
            "CNPJ": self.preset.cnpj,
            "CPF": self.preset.cpf,
            "regTrib": self.preset.regTrib,
        }
        return payload


class EnderecoSerializer(PayloadSerializer):
    def __init__(self, end: Endereco):
        self.end = end

    def serialize(self) -> dict[str, object]:
        # Implement serialization logic for Endereco
        payload = {
            "endNac": {"cMun": self.end.cMun, "CEP": self.end.cep.get()},
            "endExt": self.end.endExt.model_dump_json() if self.end.endExt else None,
            "xLgr": self.end.xLgr,
            "nro": self.end.nro,
            "xCpl": self.end.xCpl,
            "xBairro": self.end.xBairro,
        }
        return payload


class TomaSerializer(PayloadSerializer):
    def __init__(self, toma: Toma):
        self.toma = toma

    def serialize(self) -> dict[str, object]:
        payload = {
            "orgaoPublico": self.toma.identificacao.orgaoPublico,
            "CNPJ": self.toma.identificacao.cnpj.get(),  # type: ignore
            "CPF": self.toma.identificacao.cpf.get(),  # type: ignore
            "NIF": self.toma.identificacao.nif,
            "cNaoNIF": (
                self.toma.dadosFiscais.cNaoNIF if self.toma.dadosFiscais else None
            ),
            "CAEPF": self.toma.dadosFiscais.caepf if self.toma.dadosFiscais else None,
            "IM": self.toma.dadosFiscais.im if self.toma.dadosFiscais else None,
            "IE": self.toma.dadosFiscais.ie if self.toma.dadosFiscais else None,
            "xNome": self.toma.identificacao.xNome,
            "end": (
                EnderecoSerializer(self.toma.end).serialize() if self.toma.end else None
            ),
            "fone": self.toma.contato.fone if self.toma.contato else None,
            "email": self.toma.contato.email.get() if self.toma.contato else None,  # type: ignore
        }

        return payload


class ServSerializer(PayloadSerializer):
    def __init__(self, serv: Serv):
        self.serv = serv

    def serialize(self) -> dict[str, object]:
        # Implement serialization logic for Serv
        payload = {
            "locPrest": {
                "cLocPrestacao": self.serv.cLocPrestacao,
                "cPaisPrestacao": self.serv.cPaisPrestacao,
            },
            "cServ": self.serv.cServ.model_dump(),
        }
        return payload


class ValoresSerializer(PayloadSerializer):
    def __init__(self, valores: Valores):
        self.valores = valores

    def serialize(self) -> dict[str, object]:
        payload = {
            "vServPreset": {
                "vReceb": self.valores.vServPreset.vReceb,
                "vServ": self.valores.vServPreset.vServ,
            },
            "vDescCondIncond": (
                self.valores.vDescCondIncond.model_dump()
                if self.valores.vDescCondIncond
                else None
            ),
            "trib": {
                "tribMun": {
                    **self.valores.trib.tribMun.model_dump(),
                    "tribISSQN": self.valores.trib.tribMun.tribISSQN.value,
                    "tpRetISSQN": self.valores.trib.tribMun.tpRetISSQN.value,  # type: ignore
                    "tpImunidade": (
                        self.valores.trib.tribMun.tpImunidade.value  # type: ignore
                        if self.valores.trib.tribMun.tribISSQN
                        == tribmun_enums.TRIBISSQN.OP_IMUNE
                        else None
                    ),
                },
                "tribFed": (
                    self.valores.trib.tribFed.model_dump()
                    if self.valores.trib.tribFed
                    else None
                ),
                "totTrib": (
                    self.valores.trib.totTrib.model_dump()
                    if self.valores.trib.totTrib
                    else None
                ),
            },
        }
        return payload


class InfDPSSerializer(PayloadSerializer):
    def __init__(self, infDPS: InfDPS):
        self.infoDPS = infDPS

    def serialize(self) -> dict[str, object]:
        payload = {
            "tpAmb": self.infoDPS.tpAmb.value,  # type: ignore
            "dhEmi": str(self.infoDPS.dhEmi),
            "verAplic": self.infoDPS.verAplic,
            "dCompet": str(self.infoDPS.dCompet),
            # "preset": PresetSerializer(self.infoDPS.preset).serialize(),
            "toma": (
                TomaSerializer(self.infoDPS.toma).serialize()
                if self.infoDPS.toma
                else None
            ),
            "serv": ServSerializer(self.infoDPS.serv).serialize(),
            "valores": ValoresSerializer(self.infoDPS.valores).serialize(),
        }

        return payload


class NfseSerializaer(PayloadSerializer):
    def __init__(self, nfse: NFSe, infDPS: InfDPS):
        self._nfse = nfse
        self._infDPS = infDPS

    def serialize(self) -> dict[str, object]:
        payload = {
            "provedor": self._nfse.provedor.value,
            "ambiente": self._nfse.ambiente.value,
            "referencia": self._nfse.referencia,
            "infoDPS": InfDPSSerializer(self._infDPS).serialize(),
        }
        return payload
