from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import validates

from app import db


class Name(db.Model):
    __tablename__ = 'name'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __str__(self):
        return self.name
