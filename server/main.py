import webapp2
from paste import httpserver

class HelloWorldHandler(webapp2.RequestHandler) :
    def get(self) :
        self.response.write('Hello World')

routes = [
    ('/', HelloWorldHandler)
]

app = webapp2.WSGIApplication(routes,debug = True)

def main() :
    httpserver.serve(app, host='localhost', port=8080)

if __name__ == "__main__" :
    main()
