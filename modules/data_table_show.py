from flask import request


def show_all_model(Model, db):
    query = Model.query

    # search filter
    search = request.args.get("search")
    if search:
        query = query.filter(db.or_(
            Model.name.like(f"%{search}%"),
            Model.last_name.like(f"%{search}%"),
            Model.age.like(f"%{search}%")
        ))
    total = query.count()

    # sorting
    sort = request.args.get("sort")
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]
            name = s[1:]
            if name not in ["name", "last_name", "age"]:
                name = "name"
            col = getattr(Model, name)
            if direction == '-':
                col = col.desc()
            order.append(col)
        if order:
            query = query.order_by(*order)

    # pagination
    start = request.args.get("start", type=int, default=-1)
    length = request.args.get("length", type=int, default=-1)
    if start != -1 and length != -1:
        query = query.offset(start).limit(length)

    # response
    rtn = {
            "data": [user.serialize for user in query],
            "total": total
          }

    return rtn