from pydantic import BaseModel


class FilmBase(BaseModel):
    title: str
    description: str
    budget: int
    release_year: int
    genres: list[str]


class FilmCreate(FilmBase):
    pass


class FilmRead(FilmBase):
    id: int


class FilmUpdate(FilmBase):
    pass
