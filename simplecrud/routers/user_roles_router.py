from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from simplecrud.crud.user_role_crud import (
    read_user_film_associations,
    read_user_company_associations,
    create_user_role_with_film,
    update_user_role_with_film,
    create_user_role_with_company,
    update_user_role_with_company,
)
from simplecrud.schemas.user import UserFilmAssociationResponse, UserCompanyAssociationResponse
from simplecrud.database import get_db

router = APIRouter()


@router.post(
    "/users/{user_id}/films/{film_id}/roles/{role}",
    response_model=UserFilmAssociationResponse,
)
def create_user_role_with_film_route(
    user_id: int, film_id: int, role: str, db: Session = Depends(get_db)
):
    return create_user_role_with_film(db, user_id, film_id, role)


@router.put(
    "/users/{user_id}/films/{film_id}/roles/{role}",
    response_model=UserFilmAssociationResponse,
)
def update_user_role_with_film_route(
    user_id: int, film_id: int, role: str, db: Session = Depends(get_db)
):
    return update_user_role_with_film(db, user_id, film_id, role)


@router.get("/users/film/{user_id}", response_model=List[UserFilmAssociationResponse])
def get_user_films_route(
    user_id: int, db: Session = Depends(get_db)
):
    return read_user_film_associations(db, user_id)


@router.get(
    "/users/company/{user_id}", response_model=List[UserCompanyAssociationResponse]
)
def get_user_company_route(user_id: int, db: Session = Depends(get_db)):
    return read_user_company_associations(db, user_id)


@router.post(
    "/users/{user_id}/companies/{company_id}/roles/{role}",
    response_model=UserCompanyAssociationResponse,
)
def create_user_role_with_company_route(
    user_id: int, company_id: int, role: str, db: Session = Depends(get_db)
):
    return create_user_role_with_company(db, user_id, company_id, role)


@router.put(
    "/users/{user_id}/companies/{company_id}/roles/{role}",
    response_model=UserCompanyAssociationResponse,
)
def update_user_role_with_company_route(
    user_id: int, company_id: int, role: str, db: Session = Depends(get_db)
):
    return update_user_role_with_company(db, user_id, company_id, role)
