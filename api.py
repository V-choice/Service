from flask import redirect, request, render_template, jsonify, Blueprint, session, g
from models import User, Post
from db_connect import db

board = Blueprint('board', __name__)


