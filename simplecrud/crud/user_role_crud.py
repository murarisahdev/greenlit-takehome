from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


from simplecrud.models import (
    User,
    Company,
    Film,
    UserFilmAssociation,
    UserCompanyAssociation,
)

user_film_roles = ["writer", "producer", "director"]
user_company_roles = ["owner", "member"]

def get_object_or_404(db: Session, obj_id: int, model):
    obj = db.query(model).filter(model.id == obj_id).first()
    if obj is None:
        raise HTTPException(status_code=404, detail=f"{model} object not found")
    return obj


def validate_role(role: str, allowed_roles: list):
    if role not in allowed_roles:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid role. Allowed roles: {', '.join(allowed_roles)}",
        )


def create_user_role_with_film(db: Session, user_id: int, film_id: int, role: str):
    validate_role(role, user_film_roles)

    user = get_object_or_404(db, user_id, User)
    film = get_object_or_404(db, film_id, Film)

    if user is None or film is None:
        raise HTTPException(status_code=404, detail="User or Film not found")

    # Check if the association already exists
    existing_association = (
        db.query(UserFilmAssociation)
        .filter_by(user_id=user_id, film_id=film_id, role=role)
        .first()
    )

    if existing_association:
        raise HTTPException(status_code=400, detail="Association already exists")

    # Create a new association
    new_association = UserFilmAssociation(user_id=user_id, film_id=film_id, role=role)

    try:
        db.add(new_association)
        db.commit()
        db.refresh(new_association)
        return new_association
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate association entry")


def update_user_role_with_film(db: Session, user_id: int, film_id: int, role: str):
    validate_role(role, user_film_roles)

    user = get_object_or_404(db, user_id, User)
    film = get_object_or_404(db, film_id, Film)

    if user is None or film is None:
        raise HTTPException(status_code=404, detail="User or Film not found")

    # Attempt to update the association directly
    user_film_association = (
        db.query(UserFilmAssociation)
        .filter_by(user_id=user_id, film_id=film_id)
        .first()
    )

    if user_film_association is None:
        raise HTTPException(status_code=404, detail="User-Film association not found")

    # Update the role if the association exists
    user_film_association.role = role

    # Commit changes and refresh
    db.commit()
    db.refresh(user_film_association)
    return user_film_association


def read_user_film_associations(db: Session, user_id: int):
    user_film_association = (
        db.query(UserFilmAssociation)
        .filter(UserFilmAssociation.user_id == user_id)
        .all()
    )
    return user_film_association


def create_user_role_with_company(
    db: Session, user_id: int, company_id: int, role: str
):
    validate_role(role, user_company_roles)

    user = get_object_or_404(db, user_id, User)
    company = get_object_or_404(db, company_id, Company)

    if user is None or company is None:
        raise HTTPException(status_code=404, detail="User or Company not found")

    # Check if the association already exists
    existing_association = (
        db.query(UserCompanyAssociation)
        .filter_by(user_id=user_id, company_id=company_id, role=role)
        .first()
    )

    if existing_association:
        raise HTTPException(status_code=400, detail="Association already exists")

    # Create a new association
    new_association = UserCompanyAssociation(
        user_id=user_id, company_id=company_id, role=role
    )

    try:
        db.add(new_association)
        db.commit()
        db.refresh(new_association)
        return new_association
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Duplicate association entry")


def update_user_role_with_company(
    db: Session, user_id: int, company_id: int, role: str
):
    validate_role(role, user_company_roles)

    user = get_object_or_404(db, user_id, User)
    company = get_object_or_404(db, company_id, Company)

    if user is None or company is None:
        raise HTTPException(status_code=404, detail="User or Company not found")

    # Attempt to update the association directly
    user_company_association = (
        db.query(UserCompanyAssociation)
        .filter_by(user_id=user_id, company_id=company_id)
        .first()
    )

    if user_company_association is None:
        raise HTTPException(status_code=404, detail="User-Company association not found")

    # Update the role if the association exists
    user_company_association.role = role

    # Commit changes and refresh
    db.commit()
    db.refresh(user_company_association)
    return user_company_association


def read_user_company_associations(db: Session, user_id: int):
    user_company_association = (
        db.query(UserCompanyAssociation)
        .filter(UserCompanyAssociation.user_id == user_id)
        .all()
    )
    return user_company_association
