import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User, UserForm
from services.database import db


def index():
    users = User.query
    return render_template("/User/index.html", title="Tabla de Usuarios", users=users)


def store():
    form = UserForm(request.form)

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
    query = User.query

    # search filter
    search = request.args.get('search')
    if search:
        query = query.filter(db.or_(
            User.name.like(f'%{search}%'),
            User.age.like(f'%{search}%')
        ))
    total = query.count()

    # sorting
    sort = request.args.get('sort')
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ['name']:
                name = 'name'
            col = getattr(User, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get('start', type=int, default=-1)
    length = request.args.get('length', type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    # response
    rtn = {
            'data': [user.to_dict() for user in query],
            'total': total
          }

    return rtn
