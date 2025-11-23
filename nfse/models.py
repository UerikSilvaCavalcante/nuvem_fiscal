from pydantic import BaseModel, field_validator
from typing import Optional, Union, List
from datetime import date as Date
from value_objects.cnpj import CNPJ
from value_objects.cpf import CPF
from value_objects.email import Email
from decimal import Decimal
from abc import ABC, abstractmethod
from value_objects.endereco_simples import EnderecoSimples
from value_objects.endereco import Endereco
from nfse.enums import (
    piscofins_enum,
    tribmun_enums,
    dados_fiscais_enums,
)
from nfse.enums.nfse_enums import AMBIENTE, PROVEDOR


class RegTrib(BaseModel):
    regespTrib: Optional[int]


class Preset(BaseModel):
    cnpj: Optional[CNPJ]
    cpf: Optional[CPF]
    regTrib: Optional[RegTrib]


class Identificacao(BaseModel):
    orgaoPublico: Optional[bool] = False
    cnpj: Optional[CNPJ]
    cpf: Optional[CPF]
    nif: Optional[str]
    xNome: str


class DadosFiscais(BaseModel):
    im: Optional[str]
    ie: Optional[str]
    caepf: Optional[str]
    cNaoNIF: Optional[dados_fiscais_enums.CNAONIFENUM]


class Contato(BaseModel):
    fone: Optional[str]
    email: Optional[Email]


class Toma(BaseModel):
    identificacao: Identificacao
    contato: Optional[Contato]
    dadosFiscais: Optional[DadosFiscais] = None
    end: Optional[Endereco]


class LocPreset(BaseModel):
    cLocPrestacao: Optional[str]
    cPaisPrestacao: Optional[str]


class CServ(BaseModel):
    cTribNac: str
    cTribMun: Optional[str] = ""
    CNAE: Optional[str] = ""
    xDescServ: str
    cNBS: Optional[str] = ""


class ServInfo(BaseModel, ABC):
    cTribNac: str
    cTribMun: Optional[str]
    CNAE: Optional[str]
    xDescServ: str
    cNBS: Optional[str]
    cNatOp: Optional[str]
    cSitTrib: Optional[str]


class Serv(BaseModel):
    cLocPrestacao: Optional[str] = None
    cPaisPrestacao: Optional[str] = "1058"
    cServ: CServ


class VServPreset(BaseModel):
    vReceb: Optional[Decimal] = Decimal(0)
    vServ: Decimal


class VDescCondIcond(BaseModel):
    vDescIncond: Decimal
    vDescCond: Decimal


class TribMun(BaseModel):
    tribISSQN: tribmun_enums.TRIBISSQN
    cLocIncid: Optional[str] = ""
    cPaisResult: Optional[str] = "1058"

    tpImunidade: Optional[tribmun_enums.TPIMUNIDADE]

    pAliq: Optional[Decimal] = Decimal(0.00)

    tpRetISSQN: Optional[tribmun_enums.TPRETISSQN] = tribmun_enums.TPRETISSQN.N_RETIDNO


class Piscofins(BaseModel):
    CST: piscofins_enum.CST
    vPis: Optional[Decimal] = Decimal(0)
    vCofins: Optional[Decimal] = Decimal(0)
    tpRetPisCofins: Optional[piscofins_enum.TPRETPISCOFINS] = (
        piscofins_enum.TPRETPISCOFINS.NAO_RETIDO
    )


class TribFed(BaseModel):
    piscofins: Optional[Piscofins] = None

    vRetCSLL: Optional[Decimal] = None


class VTotTrib(BaseModel):
    vTotTribFed: Decimal
    vTotTribMun: Decimal
    vTotTribEst: Decimal


class PTotTrib(BaseModel):
    pTotTribFed: Decimal
    pTotTribMun: Decimal
    pTotTribEst: Decimal


class TotTrib(BaseModel):
    vTotTrib: Optional[VTotTrib] = None
    pTotTrib: Optional[PTotTrib] = None
    indTotTrib: Optional[int] = 0
    pTotTribSN: Optional[Decimal] = Decimal(0)


class Trib(BaseModel):
    tribMun: TribMun
    tribFed: Optional[TribFed] = None
    totTrib: Optional[TotTrib] = None


class Valores(BaseModel):
    vServPreset: VServPreset
    vDescCondIncond: Optional[VDescCondIcond] = None

    trib: Trib


class InfDPS(BaseModel):
    tpAmb: Optional[AMBIENTE]
    dhEmi: Date
    verAplic: Optional[str] = ""
    dCompet: Date

    toma: Toma

    serv: Serv
    valores: Valores


class NFSe(BaseModel):
    provedor: PROVEDOR = PROVEDOR.PRADAO
    ambiente: AMBIENTE
    referencia: Optional[str] = ""


class Cancelamento(BaseModel):
    codigo: Optional[str] = ""
    motivo: Optional[str] = ""
