from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SECRET_KEY'] = "dgvfjsdhgkh4755"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zxhvltmutnqjag:f159219fd92d5cba8358539c325e5c1b1ab3b946533dd445a8df2fe3a7ce9228@ec2-18-209-187-54.compute-1.amazonaws.com:5432/d7g1kvdihs5tg"
    

else:

    app.debug = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning




db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views