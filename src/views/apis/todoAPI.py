from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from sqlalchemy.exc import DBAPIError, IntegrityError

from src import models
from src.schema import Todo


@view_defaults(route_name="api_todo")
class ToDoAPIViews(object):
    def __init__(self, request):
        self.request = request
        self.view_name = "ToDoAPIViews"

    @view_config(
        request_method="GET", renderer="json", validate={"todo_list": Todo(many=True)}
    )
    def get(self):
        try:
            query = self.request.dbsession.query(models.ToDoModel)
            todo_list = query.all()
        except DBAPIError:
            return Response("Error!!!!!", content_type="text/plain", status=500)
        return {"todo_list": Todo(many=True).dump(todo_list)}

    @view_config(request_method="POST", renderer="json")
    def post(self):
        if self.request.json_body:
            sp = self.request.tm.savepoint()
            try:
                todo = models.ToDoModel()
                todo.title = self.request.json_body.get("title")
                todo.task = self.request.json_body.get("task")
                todo.priority = self.request.json_body.get("priority")
                self.request.dbsession.add(todo)
                self.request.dbsession.flush()
            except IntegrityError:
                sp.rollback()
        else:
            return {"result": "登録失敗"}
        return {"create_todo": Todo().dump(todo)}

    @view_config(request_method="DELETE", renderer="json")
    def delete(self):
        sp = self.request.tm.savepoint()
        if self.request.json_body:
            try:
                query = self.request.dbsession.query(models.ToDoModel).filter(
                    models.ToDoModel.id == self.request.json_body
                )
                target_todo = query.first()
                self.request.dbsession.delete(target_todo)
                self.request.dbsession.flush()
            except IntegrityError:
                sp.rollback()
        else:
            return {"result": "削除失敗"}
        return {"delete_todo": Todo().dump(target_todo)}
