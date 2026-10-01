# This is the file responsible for the databse models
# The databases are described here, no validation performed
# Explains how the data is stored
# This is the database representation


from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import JSON, DateTime, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from database.db import Base


class Files:
    __tablename__ = "worked_hours"

    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[String] = mapped_column()
    phone_number: Mapped[String] = mapped_column()


class Document:
    pass


class TrainResponse():
    __tablename__ = "Trains"
    train_id: Mapped[int] = mapped_column(primary_key=True)
    train_name: Mapped[String] = mapped_column()
