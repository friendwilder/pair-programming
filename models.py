from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import backref


database_name = "pair-p"
database_path = "postgres://{}/{}".format('Wilder@localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()
  migrate = Migrate(app, db)
  return db


both_users = db.Table('both_users',
    db.Column('hosting_user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    # db.Column('invited_user_id', db.Integer, db.ForeignKey('users.id'), nullable=True),
    db.Column('appointment_id', db.Integer, db.ForeignKey('appointments.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Appointment(db.Model):
    __tablename__ = 'appointments'

    id = db.Column(db.Integer, primary_key=True)
    appointment_time = db.Column(db.TIMESTAMP(), nullable=False)

    hosting_user = db.relationship('User', secondary=both_users, lazy='subquery', backref=db.backref('users', cascade='all, delete'))

    def __init__(self, appointment_time):
        self.appointment_time = appointment_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
