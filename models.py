from peewee import *
import datetime

db = SqliteDatabase('db')

class Post(Model):
    id = PrimaryKeyField()
    book_title = CharField()
    book_author = CharField()
    date = DateTimeField(default=datetime.datetime.now)
    text = TextField()
    



    class Meta:
        database = db

def initialize_db():
    db.connect()
    db.create_tables([Post],safe=True)
