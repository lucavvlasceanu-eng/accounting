from sqlalchemy import select
from sqlalchemy.orm import Session

from source.database.models.models import User, TrainResponse

def get_user_by_id(db: Session, user_id:int) -> User | None:
    statement = select(User).where(User.id == user_id)
    return db.scalar(statement)

def get_all_users(db:Session) -> User | None:
    statement = select(User)
    users = db.scalar(statement).all()
    return users

def get_user_by_phone(db:Session, email:str) -> User | None:
    statement = select(User).where(User.phone_number == email)
    return db.scalar(statement)

def create_user(db:Session, name:str, phone_number:str) -> User:
    user = User(name=name, phone_number=phone_number)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def get_train_schedule(db:Session) -> TrainResponse:
    pass


def get_mail(db:Session) -> MailResponse:
    pass
