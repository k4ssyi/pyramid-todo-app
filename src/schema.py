from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from src.models.todomodel import ToDoModel

class Todo(SQLAlchemyAutoSchema):
    class Meta:
        model = ToDoModel
        load_instance = True
        include_relationships = True
