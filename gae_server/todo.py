from google.appengine.ext import db

class Todo(db.Model) :
    todo = db.StringProperty(required=True)
    date = db.TimeProperty(required=True)
