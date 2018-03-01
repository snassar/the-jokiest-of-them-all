from flask import Flask, jsonify, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text
from datetime import datetime
import os

app = Flask(__name__)

db = SQLAlchemy(app)

basedir = os.path.abspath(os.path.dirname(__file__))

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<Joke {}>'.format(self.joke)

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.Column(db.String(128))
    joke_id = db.Column(db.Integer, db.ForeignKey('joke.id'))

    def __repr__(self):
        return '<Tags {}>'.format(self.tags)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    joke_id = db.Column(db.Integer, db.ForeignKey('joke.id'))

    def __repr__(self):
        return '<Rating {}>'.format(self.rating)

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

@app.route('/')
def list_jokes():

#    cursor.execute("show tables;")
#    data = cursor.fetchall()
#
#    res = jsonify(data)
#    return res

    return '''
<html>
    <head>
        <title>CNKJ</title>
    </head>
    <body>
        <h1>CNKJ</h1>
    </body>
</html>
'''

@app.route('/<joke_id>')
def show_joke(joke_id):

    if not joke_id:
        abort(404)

#    cursor.execute("show tables;")
#    data = cursor.fetchone()
#
#    res = jsonify(data)
#    return res

@app.route('/tags')
def list_tags():

#    cursor.execute("show tables;")
#    data = cursor.fetchall()
#
#    res = jsonify(data)
#    return res

    return '''
<html>
    <head>
        <title>CNKJ - Tags</title>
    </head>
    <body>
        <h1>TAGS</h1>
    </body>
</html>
'''

@app.route('/rankings')
def show_joke_rankings():

#    cursor.execute("show tables;")
#    data = cursor.fetchall()
#
#    res = jsonify(data)
#    return res

    return '''
<html>
    <head>
        <title>CNKJ - Ranking</title>
    </head>
    <body>
        <h1>Ranking</h1>
    </body>
</html>
'''

@app.route('/random')
def random_joke():

#    cursor.execute("show tables;")
#    data = cursor.fetchall()
#
#    res = jsonify(data)
#    return res

    return '''
<html>
    <head>
        <title>CNKJ - Random</title>
    </head>
    <body>
        <h1>Random</h1>
    </body>
</html>
'''

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
