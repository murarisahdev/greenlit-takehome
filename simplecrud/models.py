from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

user_film_association = Table(
    "user_film_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("film_id", Integer, ForeignKey("films.id")),
    Column("role", String),  # Role can be "writer", "producer", or "director"
)

user_company_association = Table(
    "user_company_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("company_id", Integer, ForeignKey("companies.id")),
    Column("role", String),  # Role can be "owner" or "member"
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    minimum_fee = Column(Integer)

    films = relationship(
        "Film", secondary=user_film_association, back_populates="users"
    )
    companies = relationship(
        "Company", secondary=user_company_association, back_populates="users"
    )


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    budget = Column(Integer)
    release_year = Column(Integer)
    genres = Column(String)
    users = relationship(
        "User", secondary=user_film_association, back_populates="films"
    )


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email_address = Column(String)
    phone_number = Column(String)
    users = relationship(
        "User", secondary=user_company_association, back_populates="companies"
    )
