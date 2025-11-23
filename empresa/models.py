from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date
from value_objects.cep import CEP
from django.core.files.uploadedfile import UploadedFile
from pathlib import Path
from empresa.enums.config_nfse_enums import *


class Endereco(BaseModel):
    logradouro: str
    numero: str
    complemento: Optional[str] = ""
    bairro: str
    cidade: Optional[str] = ""

    cep: CEP
    pais: Optional[str] = "Brasil"
    uf: str
    codigo_pais: Optional[str] = "1058"


class Empresa(BaseModel):
    cpf_cnpj: str
    nome_razao_social: str
    created_at: Optional[date] = date.today()
    updated_at: Optional[date] = date.today()
    inscricao_estadual: Optional[str] = ""
    inscricao_municipal: Optional[str] = ""
    nome_fantasia: Optional[str] = ""
    fone: Optional[str] = ""
    email: str


class Certificado(BaseModel):
    certificado: UploadedFile
    password: str

    class Config:
        arbitrary_types_allowed = True  # Permite tipos não-Pydantic

    @field_validator("certificado")
    def validar_certificado(cls, value: UploadedFile) -> UploadedFile:
        if not value.name.endswith(".pfx") or not value.name.endswith(".p12"):
            raise ValueError("Certificado deve ser do tipo .pfx ou .p12")
        return value


class ConfigNFSe(BaseModel):
    opSimpNac: opSimpNacEnum
    regApTribSN: regApTribSNEnum
    regEspTrib: regEspTribEnum
    lote: int
    serie: str
    numero: int
    login: str
    senha: str
    token: str
    incentivo_fical: bool
    ambiente: AmbienteEnum
