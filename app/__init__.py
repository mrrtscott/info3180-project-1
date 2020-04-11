from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SECRET_KEY'] = "dgvfjsdhgkh4755"
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:uwicomputing@localhost/project"
    

else:

    app.debug = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning




db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views