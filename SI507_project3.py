import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True #"reloads" the code whenever you make a change so that you don't have to manually restart the app to see changes.
app.config['SECRET_KEY'] = 'weoivasdfj13-9fa'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy


#########
######### Everything above this line is important/useful setup, not problem-solving.
#########


##### Set up Models #####

# Set up association Table between genre and directors
#collections = db.Table('collections',db.Column('album_id',db.Integer, db.ForeignKey('albums.id')),db.Column('artist_id',db.Integer, db.ForeignKey('artists.id')))

class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movie = db.relationship('Movie',backref='Genre')


class Director(db.Model):
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    movie = db.relationship('Movie',backref='Director')

    def __repr__(self):
        return "Director: {} (ID: {})".format(self.name,self.id)


class Movie(db.Model):
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64),unique=True) # Only unique title movies can exist in this data model
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id")) #ok to be null for now
    director_id = db.Column(db.Integer, db.ForeignKey("director.id")) # ok to be null for now


    def __repr__(self):
        return "Movie name: {} | Director ID: {} | Genre ID: {}".format(self.title, self.director_id, self.genre)


##### Helper functions #####

### For database additions
### Relying on global session variable above existing

def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

def get_or_create_genre(genre_name):
    genre = Genre.query.filter_by(name=genre_name).first()
    if genre:
        return genre
    else:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()
        return genre


##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html', num_movies=num_movies)

@app.route('/new/movie/<title>/<director>/<genre>/')
def new_movie(title, director, genre):
    if Movie.query.filter_by(title=title).first(): # if there is a song by that title
        return "That movie already exists! Add another movie."
    else:
        director = get_or_create_director(director)
        genre = get_or_create_genre(genre)
        movie = Movie(title=title, director_id=director.id,genre_id=genre.id)
        session.add(movie)
        session.commit()
        return "New movie: {} by {}.".format(movie.title, director.name)


@app.route('/all_directors')
def see_all_directors():
    directors = Director.query.all()
    names = []
    for a in directors:
        num_movies = len(Movie.query.filter_by(director_id=a.id).all())
        newtup = (a.name,num_movies)
        names.append(newtup) # names will be a list of tuples
    return render_template('all_directors.html',director_names=names)


if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver
