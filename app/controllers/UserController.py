import sys
from flask import render_template, redirect, url_for, request, abort, flash, current_app
from models.User import User, UserForm
from services.database import db
from modules.DataTableShow import show_all_model

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
    #users = User.query.all()

    #df = pd.DataFrame([user.serialize for user in users])
    df = pd.DataFrame({"Fruit": ["Apple", "Orange", "Bananas" , "Apple", "Oranges", "Bananas"],
                       "Amount": [4, 1, 2, 2, 4, 5],
                       "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]})
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('Views/User/show_graph.html', graphJSON=graphJSON)
