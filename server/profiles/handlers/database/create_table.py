from sqlobject import *
from model.todo import *

sqlhub.processConnection = connectionForURI('sqlite:///Users/rahulpaliwal/projects/todo/server/profiles/handlers/database/todo.db')

Todo.createTable()
