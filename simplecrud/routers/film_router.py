from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from simplecrud.database import get_db
from simplecrud.crud import film_crud
from simplecrud.schemas.film import FilmCreate, FilmRead, FilmUpdate

router = APIRouter(prefix="/films", tags=["films"])


@router.post("/", response_model=FilmRead)
def create_film(film_data: FilmCreate, db: Session = Depends(get_db)):
    return film_crud.create_film(db, film_data.dict())


@router.get("/{film_id}", response_model=FilmRead)
def read_film(film_id: int, db: Session = Depends(get_db)):
    film = film_crud.get_film(db, film_id)
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return film


@router.put("/{film_id}", response_model=FilmRead)
def update_film(
    film_id: int, updated_film_data: FilmUpdate, db: Session = Depends(get_db)
):
    film = film_crud.update_film(
        db, film_id, updated_film_data.dict(exclude_unset=True)
    )
    if film is None:
        raise HTTPException(status_code=404, detail="Film not found")
    return film
