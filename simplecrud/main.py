from fastapi import FastAPI
from typing import Union

from . import models
from .database import engine
from .routers import user_router, film_router, company_router, user_roles_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

app.include_router(user_router.router)
app.include_router(film_router.router)
app.include_router(company_router.router)
app.include_router(user_roles_router.router)
