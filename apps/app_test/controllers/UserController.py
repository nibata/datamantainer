from ..models.Group import Group
from ..services.database import db
from ..models.User import User, UserForm, users_groups
from flask import render_template, redirect, url_for, request, flash, current_app

from ..modules.DataTableShow import show_all_model
from ..modules.DataGraphShow import get_data_plotly_example

from flask_login import login_required


@login_required
def index():
    users = User.query
    
    return render_template("views/User/index.html", title="Users Table", store_url=url_for('user_bp.store'), search_key_word="", users=users)


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

            groups = Group.query
            groups = groups.filter(Group.code == "default")
            
            for group in groups:
                group_id = group.get_group_id()

            db.engine.execute(users_groups.insert(), user_id=user.id, group_id=group_id)

            db.session.commit()
            
            flash(f"The User {request.form['email']} has been created.", category="info")
            
            return redirect(url_for("user_bp.index"))

        else:
            flash("Error at validating data.", category="danger")

    return render_template("views/User/store.html", title="Create User", back_url=url_for('user_bp.index'), search_key_word=search_param, form=form)


def show(user_id):
    pass


def update(user_id):
    user = User.query.filter_by(id=user_id).first()
    
    if request.method == "POST":
        form = UserForm(request.form)

        # Creo flag para chequear si el password es el mismo del usuario o se está actualizando. 
        same_pwd = user.password == request.form["password"]
        same_mail = request.form["email"] == user.email
        mail_original = user.email

        if form.validate() or \
           (len(form.errors) == 1 and same_pwd and "Passwords must match" in form.errors.get("password", [])) or \
           ("Already exists." in form.errors.get("email", []) and same_mail and (same_pwd) or (request.form["password"] == request.form["confirm_password"])):
            user.name = request.form["name"],
            user.last_name = request.form["last_name"],
            user.age = request.form["age"],
            user.address = request.form["address"],
            user.email = request.form["email"],
            user.password = request.form["password"] if same_pwd else User.set_password(request.form["password"])
            
            db.session.commit()
            
            if same_mail:
                flash(f"The user {user.email} has been updated", category="success")
            else:
                flash(f"The user {request.form['email']} has been updated (the previous mail was {mail_original})", category="success")

            return redirect(url_for("user_bp.index"))        
    
    elif request.method == "GET":
        form = UserForm(obj=user)

    return render_template("views/User/update.html", title=f"Edit User", back_url=url_for('user_bp.index'), form=form, user_id=user_id)


def delete(user_id):
    user = User.query.filter_by(id=user_id).first()

    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        
        flash(f"The user {user.email} has been removed", category="info")
        
        return redirect(url_for("user_bp.index"))

    return render_template("views/User/delete.html", title=f"Delete User", back_url=url_for('user_bp.index'), user_id=user_id, mail=user.email)


def show_all():
    rtn = show_all_model(Model=User, db=db)

    return rtn


def show_graph():
    graphJSON = get_data_plotly_example()

    return render_template('views/User/show_graph.html', graphJSON=graphJSON)


def callback_graph_example():
    graphJSON = get_data_plotly_example(country=request.args.get("data"))
    
    return graphJSON
