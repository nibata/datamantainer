from enum import unique
from timeit import repeat
from flask_wtf import FlaskForm
from ..services.database import db
from wtforms_alchemy import ModelForm
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, widgets
from wtforms.validators import InputRequired, EqualTo

from .Group import Group

# Tabla de relacion entre users y groups (muchos a muchos). la documentacion recomienda 
# encarecidamente no realizar esta relacion con un modelo si no que con una tabla directamente
users_groups = db.Table('users_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('authentication.users.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('authentication.groups.id'), primary_key=True),
    schema = "authentication"
)

##############################################################################################
# MODELO USER (TABLA users)                                                                  #
##############################################################################################
class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"schema": "authentication"}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, info={"label": "Name"}, nullable=False)
    last_name = db.Column(db.String, info={"label": "Last Name"}, nullable=False)
    age = db.Column(db.Integer, info={"label": "Age"})
    address = db.Column(db.String(120), info={"label": "Address"})
    email = db.Column(db.String(120), info={"label": "E-mail"}, nullable=False, unique=True)
    password = db.Column(db.String(120), info={"label": "Password", "widget": widgets.PasswordInput(hide_value=False)}, nullable=False)

    # relacion de tablas muchos es a muchos contra tablas groups. No es necesario definir esta
    #  realción en la tabla groups
    users_groups = db.relationship('Group', secondary=users_groups, lazy='subquery', backref=db.backref('users', lazy=True)) 

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)
    

    def check_password(self, password):
        return check_password_hash(self.password, password)


    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True

    
    @property
    def is_anonymous(self):
        return False

    
    def get_id(self):
        return str(self.id)


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
                User.email)


    @staticmethod
    def get_sortable_fields():
        return ("name", 
                "age", 
                "last_name")


##############################################################################################
# FORMULARIO PARA MODELO                                                      VVVV           #
##############################################################################################
class UserForm(ModelForm):
    class Meta:
        model = User

    # Se agrega campo de confirm_password con el propósito de confirmar el password en 
    # caso de cambio.
    password = PasswordField("Password", 
                             [InputRequired(), 
                              EqualTo('confirm_password', 
                              message='Passwords must match')], 
                             widget=widgets.PasswordInput(hide_value=False))
    confirm_password = PasswordField("Confirm Password")

    # Esto fragmento de código no es necesario para que funcione
    # Lo que hace es asegurar el orden de los campos dado que al agregar el campo 
    # repeat_password queda en al comienzo del formulario en lugar del al final 
    # como es requerido.
    __order = ("name", "last_name", "email", "age", "address", "password", "confirm_password")

    def __iter__(self):
        fields = list(super(UserForm, self).__iter__())
        get_field = lambda field_id: next((field for field in fields if field.id == field_id))

        return (get_field(field_id) for field_id in self.__order)


##############################################################################################
# FORMULARIO PARA LOGIN                                                                      #
##############################################################################################
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
