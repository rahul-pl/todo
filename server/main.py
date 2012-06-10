import webapp2
from paste import httpserver
from handlers.hello_world_handler import HelloWorldHandler

routes = [
    ('/', HelloWorldHandler)
]

app = webapp2.WSGIApplication(routes,debug = True)

def main() :
    httpserver.serve(app, host='localhost', port=8080)

if __name__ == "__main__" :
    main()
