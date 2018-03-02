import os

from flask import Flask, render_template, request, jsonify, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, Table, create_engine, MetaData
from  sqlalchemy.sql.expression import func, select
from datetime import datetime

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "cnkj.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Joke(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String(256), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Joke: {}>".format(self.joke)

    def show_id(self):
        return "<ID: {}>".format(self.id)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return "<Rating: {}>".format(self.rating)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/5')
def show_joke():

    return render_template("5.html")

@app.route('/ranking')
def show_joke_rankings():
    return render_template("ranking.html")

@app.route('/ranking/kicks-like-chuck-norris')
def show_joke_rankings():
    return render_template("strong.html")

@app.route('/ranking/kicks-like-van-damme')
def show_joke_rankings():
    return render_template("weak.html")

@app.route('/random')
def random_joke():
     return render_template("random.html")

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
