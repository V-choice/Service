from flask import Flask, render_template, request,jsonify, session, redirect
from models import User, Post
import pymysql
from api import board
from api_visual import visual
from db_connect import db
from flask_bcrypt import Bcrypt
from bokeh.resources import INLINE
from module.Beforeafter import Beforeafter


app = Flask(__name__)
app.register_blueprint(visual)
app.register_blueprint(board)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456789@localhost:3306/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'super secret key'

db.init_app(app)
bcrypt = Bcrypt(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/first_choice',methods=["POST"])
def first_choice():
    if session['login'] is not None:
        user = User.query.filter(User.id==session['login']).first()
        first_choice = request.form.get('first_choice')
        if user.first_choice==None:
            user.first_choice=first_choice
            db.session.commit()
            return jsonify({'result':'success'})
        else:
            return jsonify({'result':'fail'})
    else:
        return redirect('/join')


@app.route('/second_choice',methods=["POST"])
def second_choice():
    if session['login'] is not None:
        user = User.query.filter(User.id==session['login']).first()
        second_choice = request.form.get('second_choice')
        if user.second_choice == None:
            user.second_choice=second_choice
            db.session.commit()
            return jsonify({'result':'success'})
        else:
            return jsonify({'result':'fail'})
    else:
        return redirect('/join')