import webapp2
import database.connection
from database.model.todo import Todo
import json

class CreateTodoHandler(webapp2.RequestHandler) :
    def post(self) :
        todo_sub = self.request.get('todo')
        Todo(todo = todo_sub)
        self.response.write('Todo created' + todo_sub)

class DeleteTodoHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Todo deleted')

class ListTodoshandler(webapp2.RequestHandler) :
    def get(self) :
        selections = Todo.select()
        data = []
        for selection in selections :
            data.append({selection.id : selection.todo})
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(data))
