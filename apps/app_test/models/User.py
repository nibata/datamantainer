from enum import unique
from .Group import Group
from timeit import repeat
from typing import Tuple, Dict
from flask_wtf import FlaskForm
from ..services.database import db
from wtforms_alchemy import ModelForm
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired, EqualTo
from wtforms import StringField, PasswordField, BooleanField, widgets
from werkzeug.security import generate_password_hash, check_password_hash

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
    # realción en la tabla groups
    users_groups = db.relationship('Group', secondary=users_groups, lazy='subquery', backref=db.backref('users', lazy=True)) 


    def __repr__(self) -> str:
        return f"<User {self.mail}>"


    @property
    def is_authenticated(self) -> bool:
        return True


    @property
    def is_active(self) -> bool: 
        return True

    
    @property
    def is_anonymous(self) -> bool:
        return False


    @property
    def serialize(self) -> Dict:
        """Objeto user serializado como dict

        Returns
        -------
        Dict
            Representacion en diccionario del objeto
        """
        return {
                    "id": self.id,
                    "name": self.name,
                    "last_name": self.last_name,
                    "age": self.age,
                    "address": self.address,
                    "email": self.email,
                    
               }


    @staticmethod
    def set_password(password: str) -> str:
        """Hashea el password proporcionado

        Parameters
        ----------
        password : str
            Password a hashear

        Returns
        -------
        str
            Password hasheado
        """
        return generate_password_hash(password)


    @staticmethod
    def get_searchable_fields() -> Tuple:
        """Se definen para uso de librerías externas cuales son los campos del modelo por lo que se puede realizar busqueda de datos en una consulta.
        Returns
        -------
        Tuple
            Tupla de atributos del modelo
        """
        return (User.name,
                User.last_name,
                User.email)


    @staticmethod
    def get_sortable_fields() -> Tuple:
        """Se definen para uso de librerías externas cuales son los campos del modelo para lo que se pueden ordenar los resultados de una consulta

        Returns
        -------
        Tuple
            Tupla de los nombres de los campos en base de datos.
        """
        return ("name", 
                "age", 
                "last_name")
    

    def get_id(self) -> str:
        """Obtiene el id de usuario actual

        Returns
        -------
        str
            id del usario
        """
        return str(self.id)

    
    def check_password(self, password: str) -> bool:
        """Chequea si el passwor proporcionado corresponde para la instacia de usuario actual. en terminos generales, toma el password sin hashear,
        lo hashea y compara con el valor registrado en base de datos.

        Parameters
        ----------
        password : str
            Password sin hashear

        Returns
        -------
        bool
            True en caso de que se correspondan los password, False en caso contrario
        """
        return check_password_hash(self.password, password)

    
    def check_group(self, code_group: str) -> bool:
        """Revisa si un usuario tiene un rol (pertenece a un grupo) o no.

        Parameters
        ----------
        code_group : str
            Nombre del grupo a chequear. Los grupos validos son los que se encuentran definidos en la tabla groups.

        Returns
        -------
        bool
            Si el usuario pertenece al grupo solicitado retorna True. Retornará False en caso de no pertenecer o de que el grupo no exista
        """

        for group in self.users_groups:
            if group.code == code_group:
                return True

        return False


##############################################################################################
# FORMULARIO PARA MODELO                                                                     #
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
