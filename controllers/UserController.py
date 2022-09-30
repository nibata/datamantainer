import sys
from flask import render_template, redirect, url_for, request, abort, flash, current_app
from models.User import User, UserForm
from services.database import db
from modules.data_table_show import show_all_model

import pandas as pd
import json
import plotly
import plotly.express as px


def index():
    users = User.query
    return render_template("/User/index.html", title="Tabla de Usuarios", store_url=url_for('user_bp.store'), search_key_word="", users=users)


def store():
    form = UserForm(request.form)

    if request.method == "POST":
        if form.validate():
            flash(request.form, category="info")
            current_app.logger.info("Se crea registro!!!!!")
            return redirect(url_for("user_bp.index"))

        else:
            flash("Error en la validación de datos", category="danger")

    return render_template("/User/store.html", title="Crear Usuario", back_url=url_for('user_bp.index'), form=form)


def show(user_id):
    ...


def update(user_id):
    users = User.query
    return render_template("/User/update.html", title=f"Tabla de Usuarios {user_id}", back_url=url_for('user_bp.index'), search_key_word="Ri",users=users)


def delete(user_id):
    ...


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

    return render_template('/User/show_graph.html', graphJSON=graphJSON)
