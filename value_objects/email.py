from pydantic import BaseModel, EmailStr


class Email(BaseModel):
    address: EmailStr

    def domain(self) -> str:
        return self.address.split("@")[1]
