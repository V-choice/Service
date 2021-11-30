from flask import redirect, request, render_template, jsonify, Blueprint, session, g
from models import User, Post
from db_connect import db

choice = Blueprint('choice', __name__)



@choice.route('/')
def hello_world():
    return render_template('index.html')

@choice.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@choice.route('/first_choice',methods=["POST"])
def first_choice():
    if session.get('login') is not None:
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


@choice.route('/second_choice',methods=["POST"])
def second_choice():
    if session.get('login') is not None:
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
