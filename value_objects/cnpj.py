from pydantic import BaseModel, field_validator
import re


class CNPJ(BaseModel):
    value: str

    @field_validator("value")
    def _one_digit(cls, value: str) -> str:
        if not value:
            raise ValueError("CEP não pode estar vazio")
        if not re.match(r"^\d+$", value):
            raise ValueError("CEP deve conter apenas números")
        return value

    @field_validator("value")
    def _valid_length(cls, value: str) -> str:
        if len(value) != 14:
            raise ValueError("CNPJ deve conter 14 números")
        return value

    def get(self) -> str:
        return self.value
