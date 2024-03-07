from sqlalchemy import Column, Integer, Text, String, ForeignKey, ARRAY
from sqlalchemy.orm import relationship
from .database import Base


class UserFilmAssociation(Base):
    __tablename__ = "user_film_association"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    film_id = Column(Integer, ForeignKey("films.id"), primary_key=True)
    role = Column(String)  # Role can be "writer", "producer", or "director"


class UserCompanyAssociation(Base):
    __tablename__ = "user_company_association"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"), primary_key=True)
    role = Column(String)  # Role can be "owner" or "member"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    minimum_fee = Column(Integer)
    films = relationship(
        "Film", secondary="user_film_association", back_populates="users"
    )
    companies = relationship(
        "Company", secondary="user_company_association", back_populates="users"
    )


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    budget = Column(Integer)
    release_year = Column(Integer)
    genres = Column(ARRAY(String))
    users = relationship(
        "User", secondary="user_film_association", back_populates="films"
    )

    @property
    def genre_list(self):
        return self.genres.split(",") if self.genres else []


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    contact_email_address = Column(String)
    phone_number = Column(String)
    users = relationship(
        "User", secondary="user_company_association", back_populates="companies"
    )
