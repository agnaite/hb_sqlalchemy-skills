"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()
app = Flask(__name__)

##############################################################################
# Part 1: Compose ORM

class Human(db.Model):
    """Human model."""

    __tablename__ = "humans"

    human_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):

        return "<name: {} {}>".format(self.fname, self.lname)

class Animal(db.Model):
    """Animal model."""

    __tablename__ = "animals"

    animal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    animal_species = db.Column(db.String(25), nullable=False)
    birth_year = db.Column(db.Integer)

    human = db.relationship('Human', backref=db.backref('animals'))

    def __repr__(self):

        return "<name: {} species: {}>".format(self.name, self.animal_species)


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///animals'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.

    connect_to_db(app)
    print "Connected to DB."
