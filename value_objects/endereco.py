from endereco_simples import EndExt
from pydantic import BaseModel
from typing import Optional
from cep import CEP


class Endereco(BaseModel):
    cMun: Optional[str]
    cep: CEP
    endExt: Optional[EndExt]
    xCpl: Optional[str]
    xLgr: str
    tpLgr: Optional[str]
    nro: str
    xBairro: str
