from enum import unique
from flask_wtf import FlaskForm
from services.database import db
from wtforms_alchemy import ModelForm
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "test_schema"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, info={"label": "Name"}, nullable=False)
    last_name = db.Column(db.String, info={"label": "Last Name"}, nullable=False)
    age = db.Column(db.Integer, info={"label": "Age"})
    address = db.Column(db.String(120), info={"label": "Address"})
    email = db.Column(db.String(120), info={"label": "E-mail"}, nullable=False, unique=True)
    password = db.Column(db.String(120), info={"label": "Password"}, nullable=False)
        

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)
    

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

    def __repr__(self):
        return '<User {}>'.format(self.email)


    @property
    def serialize(self):
        return {
                    "id": self.id,
                    "name": self.name,
                    "last_name": self.last_name,
                    "age": self.age,
                    "address": self.address,
                    "email": self.email,
                    
               }

    @staticmethod
    def get_searchable_fields():
        return (User.name,
                User.last_name,
                User.email,
                User.age)


    @staticmethod
    def get_sortable_fields():
        return ("name", 
                "age", 
                "last_name")


class UserForm(ModelForm):
    class Meta:
        model = User
        

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')
