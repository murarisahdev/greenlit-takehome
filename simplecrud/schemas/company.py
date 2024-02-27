from pydantic import BaseModel


class CompanyBase(BaseModel):
    name: str
    contact_email_address: str
    phone_number: str


class CompanyCreate(CompanyBase):
    pass


class CompanyRead(CompanyBase):
    id: int


class CompanyUpdate(CompanyBase):
    pass
