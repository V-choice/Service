from flask import redirect, request, render_template, jsonify, Blueprint, session, g
from models import User, Post
from db_connect import db
from flask_bcrypt import Bcrypt
import pendulum

#시각화 그래프 저장
import base64
from io import BytesIO

#시각화
import matplotlib.pyplot as plt


board = Blueprint('board',__name__)
bcrypt = Bcrypt()


@board.before_app_request
def load_logged_in_user():
    user_id = session.get('login')
    if login is None:
            g.user=None
    else:
            g.user=db.session.query(User).filter(User.id==user_id).first()

@board.route("/join",methods=["GET","POST"])
def join():
    if session.get('login') is None:
        if request.method == 'GET':
            return render_template('join.html')
        else:
            user_id = request.form['user_id']
            user_pw = request.form['user_pw']
            pw_hash = bcrypt.generate_password_hash(user_pw)
            
            user = User(user_id, pw_hash)
            db.session.add(user)
            db.session.commit()
            return jsonify({"result":"success"})
    else:
        return redirect('/')

@board.route('/login',methods = ['GET','POST'])
def login():
        if request.method == 'GET':
            return render_template('login.html')
            
        else:
            user_id = request.form['user_id']
            user_pw = request.form['user_pw']
            user = User.query.filter(User.user_id==user_id).first()
            
            if user is not None:
                if bcrypt.check_password_hash(user.user_pw,user_pw):
                    session['login']=user.id
                    return jsonify({'result':'success'})
                else:
                    return jsonify({'result':'fail'})
            else:
                return jsonify({'result':'fail'})

@board.route('/logout')
def logout():
    session['login'] = None
    return redirect('/login')

@board.route("/post", methods=["GET","POST"])
def post():
    if session.get('login') is not None:
        if request.method == 'GET':
            post_data = Post.query.order_by(Post.like.desc()).all()
            now = pendulum.now("UTC").naive()
            choice_data = User.query.all()
            first_yes,first_no,second_yes,second_no = [],[],[],[]
            for user in choice_data:
                if user.first_choice == 'YES':
                    first_yes.append(user.user_id)
                if user.first_choice == 'NO':
                    first_no.append(user.user_id)
                if user.second_choice == 'YES':
                    second_yes.append(user.user_id)
                if user.second_choice =='NO':
                    second_no.append(user.user_id)

            yes_yes = len(list(set(first_yes)&set(second_yes)))
            yes_no = len(list(set(first_yes)-set(second_yes))) if len(list(set(first_yes)-set(second_yes))) > 0 else len(list(set(second_yes)-set(first_yes)))
            no_yes = len(list(set(first_no)-set(second_yes))) if len(list(set(first_no)-set(second_yes))) >0 else len(list(set(second_yes)-set(first_no)))
            no_no = len(list(set(first_no)&set(second_no)))
            total = [yes_yes,yes_no,no_yes,no_no]

            sum_total = sum(total)
            centre_circle=plt.Circle((0,0),0.50,fc='white')
            plt.switch_backend('Agg') #to set the backend to a non-interactive one
            plt.figure(figsize=(12,4))
            plt.subplot(131)
            plt.pie([len(first_yes),len(first_no)],labels=["yes(%d)" %(len(first_yes)),"no(%d)" %(len(first_no))],radius=0.9,shadow=True,startangle=90,explode=(0.0,0.1),colors=["blue","red"])
            plt.title('First Choice')
            plt.axis('equal')
            plt.gcf()
            plt.gca().add_artist(centre_circle)
            plt.subplot(132)
            plt.pie([len(second_yes),len(second_no)],labels=["yes(%d)" %(len(second_yes)),"no(%d)" %(len(second_no))],radius=0.9,shadow=True,startangle=90,explode=(0.0,0.1),colors=["blue","red"])
            plt.title('Second Choice')
            plt.axis('equal')
            centre_circle2=plt.Circle((0,0),0.50,fc='white')
            plt.gcf()
            plt.gca().add_artist(centre_circle2)
            plt.subplot(133)
            plt.pie(total,labels=["yes_yes(%d)" %yes_yes,"yes_no(%d)" %yes_no,"no_yes(%d)" %no_yes,"no_no(%d)"%no_no],radius=0.9,shadow=True,colors=['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf'])
            plt.title('Choices transition')
            plt.axis('equal')
            centre_circle3=plt.Circle((0,0),0.50,fc='white')
            plt.gcf()
            plt.gca().add_artist(centre_circle3)
            plt.subplots_adjust(wspace=0.4)
            buf = BytesIO()
            plt.savefig(buf, format='png')
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            plt.close()
            return render_template("board.html"\
                , post_list = post_data, now=now, data=data,sum_total = sum_total,total=total)
        else:
            content = request.form['content']
            author = request.form['author']
            post = Post(author,content)
            db.session.add(post)
            db.session.commit()
            return jsonify({"result":"success"})
    else:
        return redirect('/join')

        
@board.route("/post", methods=["DELETE"])
def delete_post():
        id = request.form['id']
        author = request.form['author']
        data = Post.query.filter(Post.id==id,Post.author==author).first()
        if data is not None:
            db.session.delete(data)
            db.session.commit()
            return jsonify({'result':'success'})
        else:
            return jsonify({'result':'fail'})


@board.route("/post", methods=["PATCH"])
def update_post():
    id = request.form['id']
    content = request.form['content']
    author = User.query.filter(User.id==session['login']).first()
    
    data = Post.query.filter(Post.id==id,Post.author==author.user_id).first()
    data.content=content
    if len(content) == 0:
        return jsonify({'result':'fail'})
    db.session.commit()
    return jsonify({'result':'success'})

@board.route("/like", methods=["PATCH"])
def update_like():
    id = request.form['id']
    post = Post.query.filter(Post.id == id).first()
    post.like += int(1)
    db.session.commit()
    return jsonify({'result':'success'})
    
