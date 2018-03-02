from flask import Flask, jsonify, url_for, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Text, Table, create_engine, MetaData
from datetime import datetime
import os

app = Flask(__name__)

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
metadata = MetaData(bind=engine)

jokes = Table('jokes', metadata, autoload=True)
con = engine.connect()
con.execute(jokes.insert(), id='1', joke='Chuck Norris has two speeds: Walk and Kill.')

@app.route('/')
def list_jokes():

#    cursor.execute("show tables;")
    data = Jser.query.all()
    res = jsonify(data)
    return res

#    return '''
#<html>
#    <head>
#        <title>CNKJ</title>
#    </head>
#    <body>
#        <h1>CNKJ</h1>
#    </body>
#</html>
#'''

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

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
