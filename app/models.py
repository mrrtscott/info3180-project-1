from . import db
from datetime import datetime



class Profile(db.Model):
   
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    gender = db.Column(db.String(20))
    email = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100))
    biography = db.Column(db.Text())
    profile_picture = db.Column(db.String(100))
    date_joined = db.Column(db.String(100))


    def __init__(self, first_name, last_name, gender, email, location, biography, profile_picture):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_picture = profile_picture
        self.date_joined = datetime.now().strftime("%B %d, %Y")
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)