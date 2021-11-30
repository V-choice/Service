from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api.api_board import board
from api.api_visual import visual
from api.api_choice import choice
from db_connect import db
import config

app = Flask(__name__)
app.register_blueprint(visual)
app.register_blueprint(board)
app.register_blueprint(choice)
app.config.from_object(config)

db.init_app(app)

db.init_app(app)

if __name__=="__main__":
    app.run(host='0.0.0.0',port='5000',debug=True)
