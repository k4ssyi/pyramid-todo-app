from sqlalchemy import Column, Index, Integer, Text

from .meta import Base


class ToDoModel(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    task = Column(Text)
    priority = Column(Integer)
