from station import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    def set_password(self, password):
        """
        Use password hash to set the field.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)

class Caller(db.Model):
    caller = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(256), index=True, unique=True)
    code = db.Column(db.BIGINT)
    email = db.Column(db.String(132))
    active = db.Column(db.Boolean,default=False)

class Call(db.Model):
    call = db.Column(db.Integer, primary_key=True)
    caller = db.Column(db.Integer,db.ForeignKey('caller.caller'))
    callee = db.Column(db.Integer,db.ForeignKey('caller.caller'))
    active = db.Column(db.Boolean, default=True)
    block = db.Column(db.Boolean,default=False)
    assign_date = db.Column(db.DateTime,default=datetime.datetime.utcnow)

class Question(db.Model):
    question = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255),nullable=False)
    author = db.Column(db.Integer,db.ForeignKey('user.id'))
    valid = db.Column(db.Boolean, default=True)
    date_added = db.Column(db.DateTime,default=datetime.datetime.utcnow)


