from sqlobject import *

print 'connection was imported'
sqlhub.processConnection = connectionForURI('sqlite:///Users/rahulpaliwal/projects/todo/server/profiles/database/todo.db')
