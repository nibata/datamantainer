import sys
from flask import render_template, redirect, url_for, request, abort, flash, current_app
from models.User import User, UserForm
from services.database import db
from modules.DataTableShow import show_all_model
from modules.DataGraphShow import get_data_plotly_example

import pandas as pd
import json
import plotly
import plotly.express as px


def index():
    users = User.query
    return render_template("Views/User/index.html", title="Tabla de Usuarios", store_url=url_for('user_bp.store'), search_key_word="", users=users)


def store():
    form = UserForm(request.form)
    
    search_param = request.args.get("search")
    if search_param is None:
        search_param = ""

    if request.method == "POST":
        if form.validate():
            flash(request.form, category="info")
            return redirect(url_for("user_bp.index"))

        else:
            flash("Error en la validación de datos", category="danger")

    return render_template("Views/User/store.html", title="Crear Usuario", back_url=url_for('user_bp.index'), search_key_word=search_param, form=form)


def show(user_id):
    # de momento estoy utilizando este controlador para chequear si el validador de password esta funcionando
    user = User.query.filter_by(id=user_id).first()
    return str(user.check_password("pwd_test"))


def update(user_id):
    user = User.query.filter_by(id=user_id).first()
    form = UserForm(obj=user)
    return render_template("Views/User/update.html", title=f"Editar Usuario", back_url=url_for('user_bp.index'), form=form)


def delete(user_id):
    flash(f"Crear lógica de borrado de registro.\nID Usuario: {user_id}", category="danger")
    return redirect(url_for("user_bp.index"))


def show_all():
    rtn = show_all_model(Model=User, db=db)

    return rtn


def show_graph():
    graphJSON = get_data_plotly_example()

    return render_template('Views/User/show_graph.html', graphJSON=graphJSON)


def callback_graph_example():
    graphJSON = get_data_plotly_example(country=request.args.get("data"))
    return graphJSON

