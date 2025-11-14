from pydantic import BaseModel
from typing import Optional
from cep import CEP

class EndExt(BaseModel):
    cPais: str
    cEndPost: str
    xCidade:str
    xEstProvReg:str

class EnderecoSimples(BaseModel):
    cep: CEP
    endExt: Optional[EndExt]
    xLgr: str
    tpLgr: Optional[str]
    nro: str
    xBairro: str
    xCpl: Optional[str]