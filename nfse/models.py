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
    dadosFiscais: Optional[DadosFiscais]
    end: Optional[Endereco]


class Interm(BaseModel):
    identificacao: Identificacao
    contato: Optional[Contato]
    dadosFiscais: Optional[DadosFiscais]
    end: Optional[Endereco]


class LocPreset(BaseModel):
    cLocPrestacao: Optional[str]
    cPaisPrestacao: Optional[str]


class CServ(BaseModel):
    cTribNac: str
    cTribMun: Optional[str]
    CNAE: Optional[str]
    xDescServ: str
    cNBS: Optional[str]


class ServInfo(BaseModel, ABC):
    cTribNac: str
    cTribMun: Optional[str]
    CNAE: Optional[str]
    xDescServ: str
    cNBS: Optional[str]
    cNatOp: Optional[str]
    cSitTrib: Optional[str]


class Serv(BaseModel):
    cLocPrestacao: Optional[str]
    cPaisPrestacao: Optional[str]
    cServ: CServ


class VServPreset(BaseModel):
    vReceb: Optional[Decimal]
    vServ: Decimal


class VDescCondIcond(BaseModel):
    vDescIncond: Decimal
    vDescCond: Decimal


class TribMun(BaseModel):
    tribISSQN: tribmun_enums.TRIBISSQN
    cLocIncid: Optional[str]
    cPaisResult: Optional[str]

    tpImunidade: Optional[tribmun_enums.TPIMUNIDADE]

    pAliq: Optional[Decimal]

    tpRetISSQN: Optional[tribmun_enums.TPRETISSQN]


class Piscofins(BaseModel):
    CST: Optional[piscofins_enum.CST]
    vPis: Optional[Decimal]
    vCofins: Optional[Decimal]
    tpRetPisCofins: Optional[piscofins_enum.TPRETPISCOFINS]


class TribFed(BaseModel):
    piscofins: Optional[Piscofins]

    vRetCSLL: Optional[Decimal]


class VTotTrib(BaseModel):
    vTotTribFed: Optional[Decimal]
    vTotTribMun: Optional[Decimal]
    vTotTribEst: Optional[Decimal]


class PTotTrib(BaseModel):
    pTotTribFed: Optional[Decimal]
    pTotTribMun: Optional[Decimal]
    pTotTribEst: Optional[Decimal]


class TotTrib(BaseModel):
    vTotTrib: Optional[VTotTrib]
    pTotTrib: Optional[PTotTrib]
    indTotTrib: Optional[int]
    pTotTribSN: Optional[Decimal]


class Trib(BaseModel):
    tribMun: TribMun
    tribFed: Optional[TribFed] = None
    totTrib: Optional[TotTrib] = None


class Valores(BaseModel):
    vServPreset: VServPreset
    vDescCondIncond: Optional[VDescCondIcond]

    trib: Trib


class InfDPS(BaseModel):
    tpAmb: Optional[AMBIENTE]
    dhEmi: Date
    verAplic: Optional[str] = ""
    dCompet: Optional[Date]

    toma: Toma

    serv: Serv
    valores: Valores


class NFSe(BaseModel):
    provedor: PROVEDOR = PROVEDOR.PRADAO
    ambiente: AMBIENTE
    referencia: Optional[str]

    