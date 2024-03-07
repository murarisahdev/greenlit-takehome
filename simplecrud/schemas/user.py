from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    minimum_fee: int


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(UserBase):
    pass


class UserFilmAssociationResponse(BaseModel):
    user_id: int
    film_id: int
    role: str


class UserCompanyAssociationResponse(BaseModel):
    user_id: int
    company_id: int
    role: str
