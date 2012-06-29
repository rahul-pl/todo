import webapp2

class CreateTodoHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Hello World')

class DeleteTodoHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Hello World')

class ListTodoshandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Hello World')
