import datetime
import webapp2
from google.appengine.ext.webapp import template
from todo import Todo
import os

class MainPage(webapp2.RequestHandler):
	def get(self):
		todos_query = Todo.all().order('-date')
		todos = todos_query.fetch(10)
		
		template_values = {
			'todos' : todos
		}
		
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))

class CreateTodo(webapp2.RequestHandler):
	def get(self):
		todo = self.request.get('todo')
		
		todo_obj = Todo(todo=todo, date=datetime.datetime.now().time())
		todo_obj.put()
		
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Request to create ' + todo + ' received')

app = webapp2.WSGIApplication([('/', MainPage), ('/create', CreateTodo)],
							  debug=True)