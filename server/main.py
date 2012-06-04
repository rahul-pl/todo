import datetime
import webapp2
from todo import Todo

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Hello, webapp World!')

class CreateTodo(webapp2.RequestHandler):
	def get(self):
		todo = self.request.get('todo')
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.out.write('Request to create ' + todo + ' received')

app = webapp2.WSGIApplication([('/', MainPage), ('/create', CreateTodo)],
							  debug=True)