import os
import webapp2
import database.connection
from database.model.todo import Todo
from jinja2 import Environment, FileSystemLoader

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

env = Environment(loader=FileSystemLoader(path))

class TodosPageHandler(webapp2.RequestHandler) :
    def get(self) :
        selections = Todo.select()
        template = env.get_template('todos.html')
        self.response.write(template.render(
                todos = selections
            ))
