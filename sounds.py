from settings import *
import json
import datetime
db=SQLAlchemy(app)

# the class Movie will inherit the db.Model of SQLAlchemy


class Song(db.Model):
    __tablename__ = 'songs'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,
                'duration': self.duration, 'upload_time': self.upload_time}
        # this method we are defining will convert our output to json

    def add_song(self,_name, _duration, _upload_time):
        # creating an instance of our Movie constructor
        new_movie = Song(name=_name, duration=_duration, upload_time=_upload_time)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_songs(self):
        '''function to get all movies in our database'''
        return [Song.json(song) for song in Song.query.all()]

class Podcast(db.Model):
    __tablename__ = 'podcast'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    name = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name,'host':self.host,
                'duration': self.duration, 'upload_time': self.upload_time}

    def add_podcast(_name, _duration, _upload_time,_host):
        # creating an instance of our Movie constructor
        new_movie = Song(name=_name, duration=_duration, upload_time=_upload_time,host=_host)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_podcats():
        '''function to get all movies in our database'''
        return [Podcast.json(podcast) for podcast in Podcast.query.all()]

class Audiobook(db.Model):
    __tablename__ = 'audiobook'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'duration': self.duration, 'upload_time': self.upload_time,'author':self.author,'narrator':self.narrator}

    def add_audiobook(self,_title, _duration, _upload_time,_author,_narrator):
        # creating an instance of our Movie constructor
        new_movie = Song(title=_title, duration=_duration, upload_time=_upload_time,author=_author,narrator=_narrator)
        db.session.add(new_movie)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_movies(self):
        '''function to get all movies in our database'''
        return [Audiobook.json(audiobook) for audiobook in Audiobook.query.all()]