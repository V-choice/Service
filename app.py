from flask import Flask, render_template, request,jsonify, session
from models import User, Post
import pymysql
from api import board
from api_visual import visual
from db_connect import db
from flask_bcrypt import Bcrypt
from bokeh.resources import INLINE
from module.Beforeafter import Beforeafter


app = Flask(__name__)
app.register_blueprint(board)
app.register_blueprint(visual)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost:3306/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'

db.init_app(app)
bcrypt = Bcrypt(app)


@app.route('/')
def hello_world():
    # if request.method == 'POST':
    #     if request.args.get('first_choice') == 'yes':
    #         first_choice = 1
    #     else:
    #         first_choice = 0
    #     user = User.first_choice(first_choice)
    #     db.session.add(user)
    #     db.session.commit()
    return render_template('index.html')

# @app.route('/',methods=['PATCH'])
# def first_choice():
#     if User.query.filter(User.id==session['login']).first() is not None:


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/visual')
def visual():
    script18, div18, script20, div20 = Beforeafter.top5()
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    html = render_template(
        'visual.html',
        script18 = script18,
        div18 = div18,
        script20 = script20,
        div20 = div20,
        js_resources = js_resources,
        css_resources = css_resources
    )
    return html
