from flask import jsonify

from ..utils import senseless_print

from ...main import app
from ...core.database import jokes


@app.route('/random/')
def route_random():
    joke_data = []
    for joke in jokes:
        joke_data = {
            'id': joke.id,
            'joke': joke.content,
        }
        joke_data.append(joke_data)
    senseless_print()
    return jsonify(joke_data)
