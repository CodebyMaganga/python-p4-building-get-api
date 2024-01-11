#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, User, Review, Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return "Index for Game/Review/User API"

@app.route('/games')
def games():
    all_games = []

    for game in Game.query.all():
        new_game={
            'title': game.title,
            'genre': game.genre,
            'platform': game.platform,
            "price": game.price
        }
        all_games.append(new_game)
    
    response = make_response(jsonify(all_games),200)

    response.headers["Content-Type"] = "application/json"

    return response

@app.route('/games/<int:id>')
def get_game():
    game = Game.query.filter_by(id == id).first()

    result = game.to_dict()

    response = make_response(jsonify(result), 200)

    response.headers["Content-Type"] = 'application/json'

    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)