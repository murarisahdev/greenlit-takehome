from sqlalchemy.orm import Session

from simplecrud.models import Film


def create_film(db: Session, film_data: dict):
    db_film = Film(**film_data)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)
    return db_film


def get_film(db: Session, film_id: int):
    return db.query(Film).filter(Film.id == film_id).first()


def update_film(db: Session, film_id: int, updated_film_data: dict):
    db_film = get_film(db, film_id)
    if db_film:
        for key, value in updated_film_data.items():
            setattr(db_film, key, value)
        db.commit()
        db.refresh(db_film)
    return db_film
