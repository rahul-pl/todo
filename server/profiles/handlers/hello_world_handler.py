import webapp2

class HelloWorldHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Hello World')
