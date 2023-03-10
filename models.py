from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates

from app import db


class names(db.names):
    __tablename__ = 'names'
    name = Column(String(50))

    def __str__(self):
        return self.name
