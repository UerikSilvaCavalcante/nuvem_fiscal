from value_objects.endereco_simples import EndExt
from pydantic import BaseModel
from typing import Optional
from value_objects.cep import CEP


class Endereco(BaseModel):
    cMun: Optional[str]
    cep: CEP
    endExt: Optional[EndExt]
    xCpl: Optional[str]
    xLgr: str
    
    nro: str
    xBairro: str
