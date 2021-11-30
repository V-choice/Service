from secret import db_pw, secret_key

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:'+db_pw+'@localhost:3306/v_choice_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SESSION_TYPE = 'filesystem'
SECRET_KEY = secret_key
