import email
from flask import render_template, redirect, url_for, request, flash, current_app
from models.User import User, UserForm

from services.database import db

from modules.DataTableShow import show_all_model
from modules.DataGraphShow import get_data_plotly_example

from flask_login import login_required


@login_required
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
            user = User(name=request.form["name"],
                        age=request.form["age"],
                        address=request.form["address"],
                        last_name=request.form["last_name"],
                        email=request.form["email"],
                        password=User.set_password(request.form["password"]))
            
            db.session.add(user)
            db.session.commit()
            
            flash(f"Se agregó la cuenta {request.form['email']}", category="info")
            
            return redirect(url_for("user_bp.index"))

        else:
            flash("Error en la validación de datos", category="danger")

    return render_template("Views/User/store.html", title="Crear Usuario", back_url=url_for('user_bp.index'), search_key_word=search_param, form=form)


def show(user_id):
    # de momento estoy utilizando este controlador para chequear si el validador de password esta funcionando
    pass


def update(user_id):
    user = User.query.filter_by(id=user_id).first()
    
    if request.method == "POST":
        form = UserForm(request.form)

        # Creo flag para chequear si el password es el mismo del usuario o se está actualizando. 
        same_pwd = user.password == request.form["password"]
        same_mail = request.form["email"] == user.email
        mail_original = user.email

        if form.validate() or (form.errors.get("email", False) and same_mail):
            
            user.name = request.form["name"],
            user.last_name = request.form["last_name"],
            user.age = request.form["age"],
            user.address = request.form["address"],
            user.email = request.form["email"],
            user.password = request.form["password"] if same_pwd else User.set_password(request.form["password"])
            
            db.session.commit()
            
            if same_mail:
                flash(f"Se actualizó el registro de {user.email}", category="success")
            else:
                flash(f"Se actualizó el registro de {request.form['email']} (anteriormente {mail_original})", category="success")

            return redirect(url_for("user_bp.index"))
    
    elif request.method == "GET":
        form = UserForm(obj=user)

    return render_template("Views/User/update.html", title=f"Editar Usuario", back_url=url_for('user_bp.index'), form=form, user_id=user_id)


def delete(user_id):
    user = User.query.filter_by(id=user_id).first()

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        
        flash(f"Se ha eliminado al usuario {user.email}", category="info")
        
        return redirect(url_for("user_bp.index"))

    return render_template("Views/User/delete.html", title=f"Eliminar Usuario", back_url=url_for('user_bp.index'), user_id=user_id, mail=user.email)


def show_all():
    rtn = show_all_model(Model=User, db=db)

    return rtn


def show_graph():
    graphJSON = get_data_plotly_example()

    return render_template('Views/User/show_graph.html', graphJSON=graphJSON)


def callback_graph_example():
    graphJSON = get_data_plotly_example(country=request.args.get("data"))
    return graphJSON

