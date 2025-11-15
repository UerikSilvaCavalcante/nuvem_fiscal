from service.serializers.serializer_base import PayloadSerializer
from nfse.models import (
    NFSe,
    InfDPS,
    Subst,
    Preset,
    RegTrib,
    Toma,
    Interm,
    Serv,
    Valores,
)
from value_objects.endereco import Endereco


class SubstSerializer(PayloadSerializer):
    def __init__(self, subst: Subst):
        self.subst = subst

    def serialize(self) -> dict[str, object]:
        # Implement serialization logic for Subst
        payload = {
            "chSubstda": self.subst.chSubstda,
            "cMotivo": self.subst.cMotivo,
            "xMotivo": self.subst.xMotivo,
        }
        return payload


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
            "endNac": {"cMun": self.end.cMun, "CEP": self.end.cep},
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
            "CNPJ": self.toma.identificacao.cnpj,
            "CPF": self.toma.identificacao.cpf,
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
            "email": self.toma.contato.email if self.toma.contato else None,
        }

        return payload


class IntermSerializer(PayloadSerializer):
    def __init__(self, interm: Interm):
        self.interm = interm

    def serialize(self) -> dict[str, object]:
        payload = {
            "CNPJ": self.interm.identificacao.cnpj,
            "CPF": self.interm.identificacao.cpf,
            "NIF": self.interm.identificacao.nif,
            "cNaoNIF": (
                self.interm.dadosFiscais.cNaoNIF if self.interm.dadosFiscais else None
            ),
            "CAEPF": (
                self.interm.dadosFiscais.caepf if self.interm.dadosFiscais else None
            ),
            "IM": self.interm.dadosFiscais.im if self.interm.dadosFiscais else None,
            "IE": self.interm.dadosFiscais.ie if self.interm.dadosFiscais else None,
            "xNome": self.interm.identificacao.xNome,
            "end": (
                EnderecoSerializer(self.interm.end).serialize()
                if self.interm.end
                else None
            ),
            "fone": self.interm.contato.fone if self.interm.contato else None,
            "email": self.interm.contato.email if self.interm.contato else None,
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
            "comExt": self.serv.comExt.model_dump() if self.serv.comExt else None,
            "lsadppu": self.serv.lsadppu.model_dump() if self.serv.lsadppu else None,
            "obra": self.serv.obra.model_dump() if self.serv.obra else None,
            "atvEvento": (
                self.serv.atvEvento.model_dump() if self.serv.atvEvento else None
            ),
            "explRod": self.serv.explRod.model_dump() if self.serv.explRod else None,
            "infoCompl": (
                self.serv.infoCompl.model_dump() if self.serv.infoCompl else None
            ),
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
            "vDedRed": (
                self.valores.vDedRed.model_dump() if self.valores.vDedRed else None
            ),
            "trib": {
                "tribMun": self.valores.trib.tribMun.model_dump(),
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
            "tpAmb": self.infoDPS.tpAmb,
            "dhEmi": self.infoDPS.dhEmi,
            "verAplic": self.infoDPS.verAplic,
            "dCompet": self.infoDPS.dCompet,
            "subst": (
                SubstSerializer(self.infoDPS.subst).serialize()
                if self.infoDPS.subst
                else None
            ),
            "preset": PresetSerializer(self.infoDPS.preset).serialize(),
            "toma": (
                TomaSerializer(self.infoDPS.toma).serialize()
                if self.infoDPS.toma
                else None
            ),
            "interm": (
                IntermSerializer(self.infoDPS.interm).serialize()
                if self.infoDPS.interm
                else None
            ),
            "serv": ServSerializer(self.infoDPS.serv).serialize(),
            "valores": ValoresSerializer(self.infoDPS.valores).serialize(),
        }

        return payload


class EmitNfseSerializer(PayloadSerializer):
    def __init__(self, nfse: NFSe):
        self.nfse = nfse

    def serialize(self) -> dict[str, object]:
        payload = {
            "provedor": self.nfse.provedor,
            "ambiente": self.nfse.ambiente,
            "referencia": self.nfse.referencia,
            "infDPS": InfDPSSerializer(self.nfse.infDPS).serialize(),
        }
        return payload
