from pydantic import BaseModel
from typing import Optional
from value_objects.cep import CEP


class EndExt(BaseModel):
    cPais: str = "1058"
    cEndPost: Optional[str]
    xCidade: Optional[str]
    xEstProvReg: Optional[str]


class EnderecoSimples(BaseModel):
    cep: CEP
    endExt: Optional[EndExt] = None
    xLgr: str
    tpLgr: Optional[str]
    nro: str
    xBairro: str
    xCpl: Optional[str]
