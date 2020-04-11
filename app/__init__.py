from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Config Values
UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)



app.debug = True
app.config['SECRET_KEY'] = "dgvfjsdhgkh4755"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://fmtesiqeektnzz:67a23e7a9b24a1e53e068a19231c8909ec0286a74ae6ef05e4488fcc5af673fd@ec2-34-204-22-76.compute-1.amazonaws.com:5432/dat05mgb5m0o7o"
    

app.debug = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning






db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views