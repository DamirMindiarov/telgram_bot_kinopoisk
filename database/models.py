from peewee import Model, SqliteDatabase, IntegerField, CharField

db = SqliteDatabase('database.db')


class Movie(Model):
    movie_id = IntegerField()
    movie_name = CharField(null=True)
    movie_alt_name = CharField(null=True)
    movie_year = CharField(null=True)
    movie_short_description = CharField(null=True)
    movie_description = CharField(null=True)
    poster = CharField(null=True)
    genre = CharField(null=True)
    countries = CharField(null=True)

    class Meta:
        database = db


class HistoryUserMessage(Model):
    user_id = IntegerField()
    message_id = IntegerField()
    list_id_movies = CharField()

    class Meta:
        database = db


class UserHistory(Model):
    user_id = IntegerField()
    command = CharField()
    body = CharField()
    date = CharField()

    class Meta:
        database = db


db.create_tables([Movie])
db.create_tables([HistoryUserMessage])
db.create_tables([UserHistory])
