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
    exig_susp_enums,
    bm_enums,
    documentos_enums,
    expl_rod_enums,
    com_ext_enums,
    dados_fiscais_enums,
    subst_enums,
    nfse_enums,
)


class Subst(BaseModel):
    chSubstda: str
    cMotivo: subst_enums.CMOTIVO
    xMotivo: Optional[str]


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
    cNatOp: Optional[str]
    cSitTrib: Optional[str]


class ComExt(BaseModel):
    mdPrestacao: com_ext_enums.MDPRESTACAO
    vincPrest: com_ext_enums.VINCPREST
    tpMoeda: str
    vServMoeda: Decimal
    mecAFComexP: com_ext_enums.MECAFCOMEXP
    mecAFComexT: com_ext_enums.MECAFCOMEXT
    movTempBens: com_ext_enums.MOVTEMPBENS
    nDI: Optional[str]
    nRE: Optional[str]
    mdic: Optional[int]


class Lsadppu(BaseModel):
    categ: int
    objeto: int
    extensao: str
    nPostes: str


class Obra(BaseModel):
    cObra: Optional[str]
    insclmobFisc: Optional[str]
    end: EnderecoSimples


class AtvEvento(BaseModel):
    xNome: Optional[str]
    desc: Optional[str]
    end: EnderecoSimples
    dtlni: Date
    dtFim: Date
    idAtvEvt: Optional[str]
    id: Optional[str]


class ExplRod(BaseModel):
    categVeic: Optional[expl_rod_enums.CATEGVEICENUM]
    nEixos: Optional[str]
    rodagem: int
    sentido: str
    placa: str
    codAcessoPad: str
    codContrato: str


class InfoCompl(BaseModel):
    idDocTec: Optional[str]
    docRel: Optional[str]
    xInfComp: Optional[str]


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
    comExt: Optional[ComExt]
    lsadppu: Optional[Lsadppu]
    obra: Optional[Obra]
    atvEvento: Optional[AtvEvento]
    explRod: Optional[ExplRod]
    infoCompl: Optional[InfoCompl]
    
class VServPreset(BaseModel):
    vReceb: Decimal
    vServ: Decimal


class VDescCondIcond(BaseModel):
    vDescIncond: Decimal
    vDescCond: Decimal


class Nfns(BaseModel):
    nNFS: int
    modNFS: int
    serieNFS: str


class Fornec(BaseModel):
    identificacao: Identificacao
    contato: Optional[Contato]
    dadosFiscais: Optional[DadosFiscais]
    end: Optional[Endereco]


class NfseMun(BaseModel):
    cMunNFSeMun: str
    nNFSeMun: str
    cVerifNFSeMun: str


class Documentos(BaseModel):
    chNFSe: Optional[str]
    chNFe: Optional[str]
    NFSeMun: Optional[NfseMun]
    NFNFS: Optional[Nfns]
    nDocFisc: Optional[str]
    nDoc: Optional[str]
    tpDedRed: Optional[documentos_enums.TPDEDRED]
    xDescOutDed: Optional[str]
    dtEmiDoc: Date
    vDedutivelRedutivel: Decimal
    vDeducaoReducao: Decimal
    fornec: Fornec


class VDedRed(BaseModel):
    pDR: Decimal
    vDR: Decimal
    documentos: Optional[List[Documentos]]


class Bm(BaseModel):
    tpBM: bm_enums.TPBM
    nBM: str
    vRedBCBM: Optional[Decimal]
    pRedBCBM: Optional[Decimal]


class ExigSusp(BaseModel):
    tpSusp: Optional[exig_susp_enums.TPSUSP] = exig_susp_enums.TPSUSP.EXIG_SUSPENSAO
    nProcesso: str


class TribMun(BaseModel):
    tribISSQN: tribmun_enums.TRIBISSQN
    cLocIncid: Optional[str]
    cPaisResult: Optional[str]
    BM: Optional[Bm]
    exigSusp: Optional[ExigSusp]
    tpImunidade: Optional[tribmun_enums.TPIMUNIDADE]
    vBC: Optional[Decimal]
    pAliq: Optional[Decimal]
    vISSQN: Optional[Decimal]
    tpRetISSQN: Optional[tribmun_enums.TPRETISSQN]
    vLiq: Optional[Decimal]


class Piscofins(BaseModel):
    CST: Optional[piscofins_enum.CST]
    vBCPisCofins: Optional[Decimal]
    pAliqPis: Optional[Decimal]
    pAliqCofins: Optional[Decimal]
    vPis: Optional[Decimal]
    vCofins: Optional[Decimal]
    tpRetPisCofins: Optional[piscofins_enum.TPRETPISCOFINS]


class TribFed(BaseModel):
    piscofins: Optional[Piscofins]
    vRetCP: Optional[Decimal]
    vRetIRRF: Optional[Decimal]
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
    tribFed: Optional[TribFed]
    totTrib: Optional[TotTrib]


class Valores(BaseModel):
    vServPreset: VServPreset
    vDescCondIncond: Optional[VDescCondIcond]
    vDedRed: Optional[VDedRed]
    trib: Trib


class InfDPS(BaseModel):
    tpAmb: Optional[str]
    dhEmi: Date
    verAplic: Optional[Date]
    dCompet: Optional[Date]
    subst: Optional[Subst]
    preset: Preset
    toma: Optional[Toma]
    interm: Optional[Interm]
    serv: Serv
    valores: Valores


class NFSe(BaseModel):
    provedor: nfse_enums.PROVEDOR = nfse_enums.PROVEDOR.PRADAO
    ambiente: nfse_enums.AMBIENTE
    referencia: Optional[str]
    infDPS: InfDPS
