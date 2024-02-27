from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from simplecrud.database import get_db
from simplecrud.crud import company_crud
from simplecrud.schemas.company import CompanyCreate, CompanyRead, CompanyUpdate

router = APIRouter(prefix="/companies", tags=["companies"])


@router.post("/", response_model=CompanyRead)
def create_company(company_data: CompanyCreate, db: Session = Depends(get_db)):
    return company_crud.create_company(db, company_data.dict())


@router.get("/{company_id}", response_model=CompanyRead)
def read_company(company_id: int, db: Session = Depends(get_db)):
    company = company_crud.get_company(db, company_id)
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.put("/{company_id}", response_model=CompanyRead)
def update_company(
    company_id: int, updated_company_data: CompanyUpdate, db: Session = Depends(get_db)
):
    company = company_crud.update_company(
        db, company_id, updated_company_data.dict(exclude_unset=True)
    )
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company
