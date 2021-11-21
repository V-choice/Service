import os
from bokeh.resources import INLINE
from flask import Flask, render_template
import pymysql
from api import board
from db_connect import db

from module.Beforeafter import Beforeafter

app = Flask(__name__)
app.register_blueprint(board)

db.init_app(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/board')
def board():
    return render_template('board.html')

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

