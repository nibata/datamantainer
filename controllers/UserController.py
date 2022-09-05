import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User
from services.database import db


def index():
    users = User.query
    return render_template("/User/index.html", title="Tabla de Usuarios", users=users)


def store():
    ...


def show(userId):
    ...


def update(userId):
    ...


def delete(userId):
    ...


def data():
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
