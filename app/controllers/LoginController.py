from models.User import LoginForm, User
from flask import render_template, redirect, url_for, request, abort, flash, current_app
from flask_login import login_user, logout_user
from services.login_manager import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)

            flash('Bienvenido', category="success")

            return redirect(url_for("default_bp.index"))

            #next = request.args.get('next')
            
            #if not is_safe_url(next):
            #    return abort(400)

            #return redirect(next or url_for('index'))
        else:
            flash("Mail o Password erroneos", category="danger")

    return render_template('Views/Login/login.html', form=form)


def logout():
    logout_user()
    return redirect(url_for("default_bp.index"))