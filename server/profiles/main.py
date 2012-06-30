import webapp2
from m2wsgi.io.standard import WSGIHandler, Connection
from handlers.hello_world_handler import HelloWorldHandler
from handlers.todo_handler import CreateTodoHandler, DeleteTodoHandler, ListTodosHandler, TodosPageHandler

from sqlobject import *

routes = [
    ('/hello/', HelloWorldHandler),
    ('/todo', TodosPageHandler),
    ('/todo/create', CreateTodoHandler),
    ('/todo/delete', DeleteTodoHandler),
    ('/todo/list', ListTodosHandler),
]

app = webapp2.WSGIApplication(routes,debug = True)

conn = Connection(send_sock="tcp://34f9ceee-cd52-4b7f-b197-88bf2f0ec378@127.0.0.1:9997",
                  recv_sock="tcp://127.0.0.1:9996")

def main() :
    print 'Server started'
    handler = WSGIHandler(app, conn)
    handler.serve()

    sqlhub.processConnection = connectionForURI('sqlite:///Users/rahulpaliwal/projects/todo/server/profiles/handlers/database/todo.db')

if __name__ == "__main__" :
    main()
