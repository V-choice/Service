from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.api_board import board
from api.api_visual import visual
from api.api_choice import choice
from db_connect import db
import config

def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(visual)
    app.register_blueprint(board)
    app.register_blueprint(choice)
    app.config.from_object(config)


    db.init_app(app)

    from models import User, Post
    
    # cors + migration 사용해야 할 수 도 있음.
    return app



if __name__=="__main__":
    create_app().run(host='0.0.0.0',port='5000',debug=True)