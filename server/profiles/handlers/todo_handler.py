import webapp2
import database.connection
from database.model.todo import Todo
import json

class TodosPageHandler(webapp2.RequestHandler) :
    def get(self) :
        selections = Todo.select()
        response_string = ''
        for selection in selections :
            response_string += str(selection.id) + ' -> ' + selection.todo + '<br>'
        self.response.write(response_string)

class CreateTodoHandler(webapp2.RequestHandler) :
    def post(self) :
        todo_sub = self.request.get('todo')
        Todo(todo = todo_sub)
        self.response.write('Todo created' + todo_sub)

class DeleteTodoHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Todo deleted')

class ListTodosHandler(webapp2.RequestHandler) :
    def get(self) :
        selections = Todo.select()
        data = []
        for selection in selections :
            data.append({selection.id : selection.todo})
        self.response.headers['Content-Type'] = "application/json"
        self.response.write(json.dumps(data))
