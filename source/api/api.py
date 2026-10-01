from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from database.db import get_db
from source.database.models.models import User
import database.queries.queries as query
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users", response_model="UserResponse")
def return_users(db:Session = Depends(get_db)):
    users = query.get_all_users(db)

    if users is None:
        raise HTTPException(
            status_code=404,
            detail="There are no users in the database"
        )


@app.get("/get_trains", response_model="Train schedule")
def get_train_schedule(db:Session = Depends(get_db)):
    trains = query.get_train_schedule()
