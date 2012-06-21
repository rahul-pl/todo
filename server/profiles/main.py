import webapp2
from m2wsgi.io.standard import WSGIHandler, Connection
from handlers.hello_world_handler import HelloWorldHandler

routes = [
    ('/hello/', HelloWorldHandler)
]

app = webapp2.WSGIApplication(routes,debug = True)

conn = Connection(send_sock="tcp://34f9ceee-cd52-4b7f-b197-88bf2f0ec378@127.0.0.1:9997",
                  recv_sock="tcp://127.0.0.1:9996")

def main() :
    print 'Server started'
    handler = WSGIHandler(app, conn)
    handler.serve()

if __name__ == "__main__" :
    main()
