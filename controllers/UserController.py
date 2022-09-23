import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User, UserForm
from services.database import db
from modules.data_table_show import show_all_model

def index():
    users = User.query
    return render_template("/User/index.html", title="Tabla de Usuarios", users=users)


def store():
    form = UserForm(request.form)
    for field in form:
        for property, value in vars(field).items():
            print(property, ":", value)

    if request.method == "POST":
        pass

    return render_template("/User/store.html", form=form)


def show(user_id):
    ...


def update(user_id):
    users = User.query
    return render_template("/User/update.html", title=f"Tabla de Usuarios {user_id}", users=users)


def delete(user_id):
    ...


def show_all():
    rtn = show_all_model(Model=User, db=db)

    return rtn
