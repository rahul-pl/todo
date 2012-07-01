from sqlobject import *

print 'connection was imported'
sqlhub.processConnection = connectionForURI('sqlite:///Users/rahulpaliwal/projects/todo/todo.db')
