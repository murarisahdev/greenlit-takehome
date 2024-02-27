from sqlalchemy.orm import Session

from simplecrud.models import Company


def create_company(db: Session, company_data: dict):
    db_company = Company(**company_data)
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def get_company(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def update_company(db: Session, company_id: int, updated_company_data: dict):
    db_company = get_company(db, company_id)
    if db_company:
        for key, value in updated_company_data.items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
    return db_company
